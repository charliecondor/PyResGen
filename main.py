from fpdf import FPDF


def un_factored():
    resume_pdf = FPDF()
    resume_pdf.add_page()
    resume_pdf.set_font('Arial', 'B', 16)
    # resume_pdf.cell(40, 10, 'Hello2')
    resume_pdf.cell(0, 0, 'Dimensions (mm)')
    resume_pdf.line(10, 20, 200, 20)

    resume_pdf.output('test_resume.pdf', 'F')
    return


# Generates a page with horizontal and vertical dimensions listed as millimeters
def dimensions():
    dim_pdf = FPDF()
    dim_pdf.add_page()
    dim_pdf.set_auto_page_break(auto='off', margin=0)
    dim_pdf.set_font('Arial', '', 10)
    dim_pdf.cell(0, 0, 'Dimensions (mm)')
    dim_pdf.line(10, 20, 200, 20)
    dim_pdf.line(105, 10, 105, 290)

    i = 10
    dim_pdf.set_y(25)
    while i < 210:
        dim_pdf.line(i, 15, i, 25)
        dim_pdf.cell(10, 0, str(i))
        i += 10

    i = 10
    while i < 297:
        dim_pdf.line(100, i, 110, i)
        dim_pdf.set_y(i)
        dim_pdf.cell(100)
        dim_pdf.cell(10, 0, str(i))
        i += 10

    dim_pdf.output('dimensions.pdf', 'F')
    return


# Main
if __name__ == '__main__':
    # un_factored()
    dimensions()
