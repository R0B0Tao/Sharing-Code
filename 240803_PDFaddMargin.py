import fitz
import os

input_pdf = os.path.expanduser(r"C:\Users\Marce\Downloads\Download\aerobic.pdf")
output_pdf = os.path.expanduser(r"C:\Users\Marce\Downloads\Download\aerobic_margin.pdf")

def add_margin_to_pdf(input_pdf, output_pdf, margin_ratio=0.2):
    print(f"Processing {input_pdf}...")
    
    # Open PDF Files
    src_doc = fitz.open(input_pdf)
    print(f"Opened {input_pdf}, total pages: {len(src_doc)}")
    
    output_doc = fitz.open()
    
    for page_num in range(len(src_doc)):
        page = src_doc.load_page(page_num)
        
        # Get current size
        rect = page.rect
        width = rect.width
        height = rect.height
        
        # Get new size with margin
        new_width = width * (1 + 2 * margin_ratio)
        new_height = height * (1 + 2 * margin_ratio)
        
        new_page = output_doc.new_page(width=new_width, height=new_height)
              
        # Position of the original content in new page
        x0 = (new_width - width) / 2
        y0 = (new_height - height) / 2
        x1 = x0 + width
        y1 = y0 + height
        
        new_page.show_pdf_page(fitz.Rect(x0, y0, x1, y1), src_doc, page_num)
        
        print(f"Processed page {page_num + 1}: original size ({width}x{height}), new size ({new_width}x{new_height})")
    
    # Output
    output_doc.save(output_pdf)
    print(f"Output saved as {output_pdf}")
