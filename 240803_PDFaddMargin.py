import fitz  # PyMuPDF
import os

input_pdf = os.path.expanduser(r"C:\Users\Marce\Downloads\Download\aerobic.pdf")
output_pdf = os.path.expanduser(r"C:\Users\Marce\Downloads\Download\aerobic_margin.pdf")

def add_margin_to_pdf(input_pdf, output_pdf, margin_ratio=0.2):
    print(f"Processing {input_pdf}...")
    
    # 打开输入的PDF文件
    src_doc = fitz.open(input_pdf)
    print(f"Opened {input_pdf}, total pages: {len(src_doc)}")
    
    # 创建一个新的文档
    output_doc = fitz.open()
    
    # 遍历PDF的每一页
    for page_num in range(len(src_doc)):
        page = src_doc.load_page(page_num)
        
        # 获取当前页面的尺寸
        rect = page.rect
        width = rect.width
        height = rect.height
        
        # 计算增加白边后的新尺寸
        new_width = width * (1 + 2 * margin_ratio)
        new_height = height * (1 + 2 * margin_ratio)
        
        # 创建一个新的页面，用于放置原始页面和白边
        new_page = output_doc.new_page(width=new_width, height=new_height)
              
        # 计算原始页面在新页面中的中心位置
        x0 = (new_width - width) / 2
        y0 = (new_height - height) / 2
        x1 = x0 + width
        y1 = y0 + height
        
        # 将原始页面放置到新的页面中
        new_page.show_pdf_page(fitz.Rect(x0, y0, x1, y1), src_doc, page_num)
        
        # 打印调试信息
        print(f"Processed page {page_num + 1}: original size ({width}x{height}), new size ({new_width}x{new_height})")
    
    # 保存输出的PDF文件
    output_doc.save(output_pdf)
    print(f"Output saved as {output_pdf}")

# 使用示例
add_margin_to_pdf(input_pdf, output_pdf, margin_ratio=0.2)