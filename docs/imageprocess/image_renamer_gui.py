import re
import shutil
import uuid
from dataclasses import dataclass
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
    ".webp",
    ".tif",
    ".tiff",
}

MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[[^\]]*]\(([^)]+)\)")


@dataclass
class MatchedImage:
    source_path: Path
    markdown_index: int


def natural_sort_key(text: str):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def is_supported_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS


def discover_image_files(images_root: Path):
    return sorted(
        [item for item in images_root.rglob("*") if item.is_file() and is_supported_image(item)],
        key=lambda item: natural_sort_key(str(item.relative_to(images_root)).replace("\\", "/")),
    )


def collect_markdown_image_matches(markdown_content: str):
    return [(markdown_index, match.group(1).strip()) for markdown_index, match in enumerate(MARKDOWN_IMAGE_PATTERN.finditer(markdown_content))]


def build_target_name(base_name: str, index: int, source_path: Path) -> str:
    return f"{base_name}{index}{source_path.suffix.lower()}"


def rename_images(matched_images, base_name: str):
    temp_records = []
    renamed_records = []

    for matched in matched_images:
        source = matched.source_path
        temp_name = f"__renaming__{uuid.uuid4().hex}{source.suffix.lower()}"
        temp_path = source.parent / temp_name
        source.rename(temp_path)
        temp_records.append((matched, source, temp_path))

    try:
        for display_index, (matched, original_path, temp_path) in enumerate(temp_records, start=1):
            target_name = build_target_name(base_name, display_index, original_path)
            target_path = original_path.parent / target_name
            if target_path.exists():
                raise ValueError(f"目标文件已存在：{target_path.name}")
            temp_path.rename(target_path)
            renamed_records.append((matched, original_path, target_path))
    except Exception:
        for _, original_path, temp_path in temp_records:
            if temp_path.exists():
                temp_path.rename(original_path)
        raise

    return renamed_records


def update_markdown_content(markdown_content: str, markdown_dir: Path, renamed_records):
    replacement_by_index = {}
    for matched, _, target_path in renamed_records:
        relative_path = target_path.relative_to(markdown_dir).as_posix()
        replacement_by_index[matched.markdown_index] = f"![]({relative_path})"

    current_index = 0

    def replacer(match):
        nonlocal current_index
        updated = replacement_by_index.get(current_index, match.group(0))
        current_index += 1
        return updated

    return MARKDOWN_IMAGE_PATTERN.sub(replacer, markdown_content)


def build_matched_images(markdown_matches, image_files):
    replace_count = min(len(markdown_matches), len(image_files))
    matched_images = []
    for index in range(replace_count):
        markdown_index, _ = markdown_matches[index]
        matched_images.append(MatchedImage(source_path=image_files[index], markdown_index=markdown_index))
    return matched_images


def process_images_and_markdown(base_name: str, markdown_path: str, images_root_path: str, force_replace: bool):
    markdown_file = Path(markdown_path).expanduser().resolve()
    markdown_dir = markdown_file.parent
    images_root = Path(images_root_path).expanduser().resolve()

    if not markdown_file.exists() or not markdown_file.is_file() or markdown_file.suffix.lower() != ".md":
        raise ValueError("请选择有效的 .md 文档。")
    if not images_root.exists() or not images_root.is_dir():
        raise ValueError(f"未找到图片目录：{images_root}")
    if not base_name.strip():
        raise ValueError("图片名称前缀不能为空。")

    markdown_content = markdown_file.read_text(encoding="utf-8")
    markdown_matches = collect_markdown_image_matches(markdown_content)
    if not markdown_matches:
        raise ValueError("Markdown 中没有找到可处理的图片标记。")

    image_files = discover_image_files(images_root)
    if not image_files:
        raise ValueError(f"{images_root} 下没有找到支持的图片文件。")

    markdown_count = len(markdown_matches)
    image_count = len(image_files)
    if markdown_count != image_count and not force_replace:
        raise RuntimeError(f"COUNT_MISMATCH:{image_count}:{markdown_count}")

    matched_images = build_matched_images(markdown_matches, image_files)
    if not matched_images:
        raise ValueError("没有可处理的图片和 Markdown 图片标记。")

    renamed_records = rename_images(matched_images, base_name)

    backup_path = markdown_file.with_suffix(markdown_file.suffix + ".bak")
    shutil.copy2(markdown_file, backup_path)

    try:
        updated_content = update_markdown_content(markdown_content, markdown_dir, renamed_records)
        markdown_file.write_text(updated_content, encoding="utf-8")
    except Exception:
        if backup_path.exists():
            shutil.copy2(backup_path, markdown_file)
        raise

    return {
        "image_count": image_count,
        "markdown_count": markdown_count,
        "replaced_count": len(renamed_records),
        "renamed_names": [target_path.relative_to(images_root).as_posix() for _, _, target_path in renamed_records],
        "backup_path": str(backup_path),
        "markdown_path": str(markdown_file),
        "images_root": str(images_root),
        "unresolved_paths": [],
    }


class ImageRenamerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("图片与 Markdown 批量处理")
        self.root.geometry("840x520")
        self.root.resizable(False, False)

        self.doc_var = tk.StringVar()
        self.image_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.status_var = tk.StringVar(value="请先选择 Markdown 文档，再选择图片目录，最后填写图片名称前缀。")

        self.build_ui()

    def build_ui(self):
        container = tk.Frame(self.root, padx=20, pady=20)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="1. 选择 Markdown 文档", anchor="w").grid(row=0, column=0, sticky="w")
        tk.Entry(container, textvariable=self.doc_var, width=72).grid(row=1, column=0, padx=(0, 10), sticky="we")
        tk.Button(container, text="导入文档", command=self.choose_markdown, width=12).grid(row=1, column=1, sticky="e")

        tk.Label(container, text="2. 选择图片路径", anchor="w").grid(row=2, column=0, pady=(16, 0), sticky="w")
        tk.Entry(container, textvariable=self.image_var, width=72).grid(row=3, column=0, padx=(0, 10), sticky="we")
        tk.Button(container, text="导入图片", command=self.choose_image_folder, width=12).grid(row=3, column=1, sticky="e")

        tk.Label(container, text="3. 填写图片名称前缀", anchor="w").grid(row=4, column=0, pady=(16, 0), sticky="w")
        tk.Entry(container, textvariable=self.name_var, width=72).grid(row=5, column=0, columnspan=2, sticky="we")

        tk.Button(container, text="处理图片", command=self.handle_process, height=2).grid(
            row=6, column=0, columnspan=2, pady=22, sticky="we"
        )

        tk.Label(
            container,
            text=(
                "处理规则：\n"
                "1. 用户手动选择 Markdown 文档\n"
                "2. 用户手动选择图片目录，例如同级的 _image 或 _images\n"
                "3. 图片目录按名称自然排序递归搜索，可包含多个子文件夹\n"
                "4. 只要 Markdown 中存在图片标记，就按顺序依次替换，不做强关联匹配\n"
                "5. 修改 Markdown 前会自动生成同目录备份文件 .md.bak"
            ),
            justify="left",
            fg="#444444",
        ).grid(row=7, column=0, columnspan=2, sticky="w")

        tk.Label(container, textvariable=self.status_var, anchor="w", fg="#006400", justify="left").grid(
            row=8, column=0, columnspan=2, pady=(18, 0), sticky="w"
        )

        container.grid_columnconfigure(0, weight=1)

    def choose_markdown(self):
        file_path = filedialog.askopenfilename(
            title="选择 Markdown 文档",
            filetypes=[("Markdown Files", "*.md")],
        )
        if file_path:
            self.doc_var.set(file_path)
            self.status_var.set("已选择 Markdown 文档，请继续选择图片目录。")

    def choose_image_folder(self):
        folder = filedialog.askdirectory(title="选择图片目录")
        if folder:
            self.image_var.set(folder)
            self.status_var.set("已选择图片目录，请填写图片名称前缀。")

    def handle_process(self):
        markdown_path = self.doc_var.get().strip()
        image_path = self.image_var.get().strip()
        base_name = self.name_var.get().strip()

        try:
            result = process_images_and_markdown(base_name, markdown_path, image_path, force_replace=False)
        except RuntimeError as exc:
            message = str(exc)
            if message.startswith("COUNT_MISMATCH:"):
                _, image_count, markdown_count = message.split(":")
                should_continue = messagebox.askyesno(
                    "数量不一致",
                    (
                        f"图片数量：{image_count}\n"
                        f"Markdown 图片标记数量：{markdown_count}\n\n"
                        "数量不一致时，会只按较小数量依次处理。\n"
                        "是否继续？"
                    ),
                )
                if not should_continue:
                    self.status_var.set("已取消处理，请检查 Markdown 图片标记数量和图片目录中的文件数量。")
                    return

                try:
                    result = process_images_and_markdown(base_name, markdown_path, image_path, force_replace=True)
                except Exception as inner_exc:
                    self.status_var.set("处理失败。")
                    messagebox.showerror("错误", str(inner_exc))
                    return
            else:
                self.status_var.set("处理失败。")
                messagebox.showerror("错误", message)
                return
        except Exception as exc:
            self.status_var.set("处理失败。")
            messagebox.showerror("错误", str(exc))
            return

        self.status_var.set(
            f"处理完成：重命名 {result['replaced_count']} 张图片，更新 {result['replaced_count']} 处 Markdown 引用。"
        )

        preview = "\n".join(result["renamed_names"][:10])
        if len(result["renamed_names"]) > 10:
            preview += "\n..."

        messagebox.showinfo(
            "处理完成",
            (
                f"图片目录：{result['images_root']}\n"
                f"图片总数：{result['image_count']}\n"
                f"Markdown 图片标记数：{result['markdown_count']}\n"
                f"实际更新数量：{result['replaced_count']}\n\n"
                f"备份文件：{result['backup_path']}\n\n"
                f"前 10 个重命名结果：\n{preview}"
            ),
        )


def main():
    root = tk.Tk()
    app = ImageRenamerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
