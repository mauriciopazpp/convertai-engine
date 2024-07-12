import re
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal

def correct_text(text):
    corrected_text = text.replace("8'^", "8º")
    return corrected_text

def remove_specific_newlines_and_join(text):
    # Define a regex pattern to match " \n" but not ". \n"
    pattern = r'(?<!\.) \n'
    # Use re.sub to replace the matched pattern with an empty string
    cleaned_text = re.sub(pattern, '', text)
    # Join the lines and preserve the new line for ". \n"
    return cleaned_text.replace('\n', '')

def get_text(element):
    if isinstance(element, (LTTextBoxHorizontal, LTTextLineHorizontal)):
        return remove_specific_newlines_and_join(
            correct_text(
                element.get_text()
            )
        )
    return None
