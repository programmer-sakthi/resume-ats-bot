import os

from paddleocr import PaddleOCR

# LOAD MODEL ONCE
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    engine="paddle",
)

def scan_resume(
    file_path: str,
    output_dir: str
):

    result = ocr.predict(file_path)

    output_images = []

    for index, res in enumerate(result):

        image_path = os.path.join(
            output_dir,
            f"scanned_{index}.jpg"
        )

        # SAVE OCR VISUALIZATION
        res.save_to_img(image_path)

        output_images.append(image_path)

    return output_images