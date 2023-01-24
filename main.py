from fpdf import FPDF

def un_factored():
    resume_pdf = FPDF()
    resume_pdf.add_page()
    resume_pdf.set_font('Arial', 'B', 16)
    resume_pdf.cell(40, 10, 'Hello2')
    resume_pdf.output('test_resume.pdf', 'F')
    return


# Main
if __name__ == '__main__':
    un_factored()
