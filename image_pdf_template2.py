from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO
import os

def create_two_column_resume(data):
    """
    Create a two-column professionally styled resume PDF
    
    Args:
        data (dict): Dictionary containing resume information
        
    Returns:
        BytesIO: PDF file as a BytesIO object
    """
    # Create a BytesIO buffer
    buffer = BytesIO()
    
    # Create the PDF document
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Path to images
    img_path = os.path.join('static', 'img', 'resume_1')
    
    # Flowable elements for the document
    elements = []
    
    # Define colors
    blue_color = colors.HexColor('#8292ee')  # Blue color used in template
    light_blue = colors.HexColor('#e6e9fa')  # Light blue for backgrounds
    text_color = colors.HexColor('#333333')  # Dark gray
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=24,
        alignment=0,  # Left aligned
        textColor=text_color,
        spaceAfter=6
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=blue_color,
        spaceBefore=12,
        spaceAfter=6,
        leading=16
    )
    
    normal_style = ParagraphStyle(
        'NormalText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=text_color,
        spaceAfter=3
    )
    
    info_style = ParagraphStyle(
        'InfoText',
        parent=normal_style,
        fontSize=11,
        fontName='Helvetica-Bold',
        spaceAfter=2,
        leading=16
    )
    
    about_style = ParagraphStyle(
        'AboutText',
        parent=normal_style,
        fontSize=10,
        alignment=4,  # Justified
        textColor=text_color
    )
    
    # Add name at the top
    elements.append(Paragraph(data['name'], name_style))
    
    # Add about text if available
    if data.get('uaboutself'):
        elements.append(Paragraph(data['uaboutself'], about_style))
    
    elements.append(Spacer(1, 0.2*inch))
    
    # Create the two-column layout
    # Left column: Personal info, Skills
    # Right column: Career objectives, Education, Achievements
    
    # First row: About Me (left) and Career Objectives (right)
    left_col_width = 2.5*inch
    right_col_width = 4*inch
    
    # ABOUT ME SECTION - LEFT COLUMN
    about_icon = Image(os.path.join(img_path, 'about_us_icon.png'))
    about_icon.drawHeight = 0.3*inch
    about_icon.drawWidth = 0.3*inch
    
    about_title = Table([[about_icon, Paragraph('<b>ABOUT ME</b>', section_title_style)]], 
                        colWidths=[0.4*inch, 2.1*inch])
    about_title.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    
    # About divider
    about_divider = Table([['']],  colWidths=[left_col_width], rowHeights=[1])
    about_divider.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 0.5, blue_color),
    ]))
    
    # DOB info
    dob_icon = Image(os.path.join(img_path, 'birthday.png'))
    dob_icon.drawHeight = 0.25*inch
    dob_icon.drawWidth = 0.25*inch
    dob_row = Table([[dob_icon, Paragraph(data['dob'], info_style)]], 
                   colWidths=[0.4*inch, 2.1*inch])
    dob_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    
    # Phone info
    phone_icon = Image(os.path.join(img_path, 'phone.png'))
    phone_icon.drawHeight = 0.25*inch
    phone_icon.drawWidth = 0.25*inch
    phone_row = Table([[phone_icon, Paragraph(data['phnum'], info_style)]], 
                     colWidths=[0.4*inch, 2.1*inch])
    phone_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    
    # Location info
    location_icon = Image(os.path.join(img_path, 'location.png'))
    location_icon.drawHeight = 0.25*inch
    location_icon.drawWidth = 0.25*inch
    location_row = Table([[location_icon, Paragraph(f"{data['city']}, {data['state']}", info_style)]], 
                        colWidths=[0.4*inch, 2.1*inch])
    location_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    
    # Email info
    email_icon = Image(os.path.join(img_path, 'email.png'))
    email_icon.drawHeight = 0.25*inch
    email_icon.drawWidth = 0.25*inch
    email_row = Table([[email_icon, Paragraph(data['email'], info_style)]], 
                     colWidths=[0.4*inch, 2.1*inch])
    email_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    
    # SKILLS SECTION - LEFT COLUMN
    skills_icon = Image(os.path.join(img_path, 'computer.png'))
    skills_icon.drawHeight = 0.3*inch
    skills_icon.drawWidth = 0.3*inch
    
    skills_title = Table([[skills_icon, Paragraph('<b>PERSONAL SKILLS</b>', section_title_style)]], 
                         colWidths=[0.4*inch, 2.1*inch])
    skills_title.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    
    # Skills divider
    skills_divider = Table([['']],  colWidths=[left_col_width], rowHeights=[1])
    skills_divider.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 0.5, blue_color),
    ]))
    
    # Skills list
    skills_content = []
    if data['skills']:
        for skill in data['skills']:
            skills_content.append(Paragraph(f"• {skill}", normal_style))
    
    # PERSONAL DETAILS - LEFT COLUMN
    personal_details = []
    personal_details.append(Paragraph(f"<b>Father's Name:</b> {data['fname']}", normal_style))
    personal_details.append(Paragraph(f"<b>Mother's Name:</b> {data['mname']}", normal_style))
    personal_details.append(Paragraph(f"<b>Permanent Address:</b> {data['paddress']}", normal_style))
    
    # CAREER OBJECTIVES - RIGHT COLUMN
    career_title = Paragraph('<b>Career Objectives</b>', section_title_style)
    career_content = Paragraph(data['ucareerob'] if data['ucareerob'] else "", normal_style)
    
    # Career divider
    career_divider = Table([['']],  colWidths=[right_col_width], rowHeights=[1])
    career_divider.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 0.5, blue_color),
    ]))
    
    # EDUCATION - RIGHT COLUMN
    education_data = []
    if data['education']:
        for edu in data['education']:
            if 'course' in edu and 'college' in edu and 'graduation' in edu:
                course_row = [
                    [Paragraph(f"<b>{edu['course']}</b>", normal_style)],
                    [Paragraph(edu['college'], normal_style)],
                    [Paragraph(f"Graduate, {edu['graduation']}", normal_style)]
                ]
                education_data.append(course_row)
    
    # ACHIEVEMENTS - RIGHT COLUMN
    achievements_icon = Image(os.path.join(img_path, 'achiements.png'))
    achievements_icon.drawHeight = 0.3*inch
    achievements_icon.drawWidth = 0.3*inch
    
    achievements_title = Table([[achievements_icon, Paragraph('<b>ACHIEVEMENTS</b>', section_title_style)]], 
                              colWidths=[0.4*inch, 3.6*inch])
    achievements_title.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    
    # Achievements divider
    achievements_divider = Table([['']],  colWidths=[right_col_width], rowHeights=[1])
    achievements_divider.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 0.5, blue_color),
    ]))
    
    # Achievements list
    achievements_content = []
    if data['achievements']:
        for achievement in data['achievements']:
            achievements_content.append(Paragraph(f"• {achievement}", normal_style))
    
    # Now build the two-column layout
    # Main table structure with left and right columns
    left_column_content = []
    
    # Add About Me section to left column
    left_column_content.append(about_title)
    left_column_content.append(about_divider)
    left_column_content.append(Spacer(1, 0.1*inch))
    left_column_content.append(dob_row)
    left_column_content.append(Spacer(1, 0.05*inch))
    left_column_content.append(phone_row)
    left_column_content.append(Spacer(1, 0.05*inch))
    left_column_content.append(location_row)
    left_column_content.append(Spacer(1, 0.05*inch))
    left_column_content.append(email_row)
    left_column_content.append(Spacer(1, 0.2*inch))
    
    # Add Skills section to left column
    left_column_content.append(skills_title)
    left_column_content.append(skills_divider)
    left_column_content.append(Spacer(1, 0.1*inch))
    for skill_item in skills_content:
        left_column_content.append(skill_item)
    left_column_content.append(Spacer(1, 0.2*inch))
    
    # Add Personal Details to left column
    for detail in personal_details:
        left_column_content.append(detail)
        left_column_content.append(Spacer(1, 0.05*inch))
    
    # Right column content
    right_column_content = []
    
    # Add Career Objectives section to right column
    right_column_content.append(career_title)
    right_column_content.append(career_content)
    right_column_content.append(Spacer(1, 0.1*inch))
    right_column_content.append(career_divider)
    right_column_content.append(Spacer(1, 0.2*inch))
    
    # Add Education section to right column
    if education_data:
        for edu_item in education_data:
            for row in edu_item:
                right_column_content.append(row[0])
            right_column_content.append(Spacer(1, 0.1*inch))
    
    # Add Achievements section to right column
    right_column_content.append(achievements_title)
    right_column_content.append(achievements_divider)
    right_column_content.append(Spacer(1, 0.1*inch))
    for achievement_item in achievements_content:
        right_column_content.append(achievement_item)
    
    # Create a table for the two-column layout
    column_gap = 0.5*inch
    
    # Pack the left and right columns into tables
    left_column = []
    for item in left_column_content:
        if isinstance(item, Spacer):
            left_column.append([item])
        else:
            left_column.append([item])
    
    right_column = []
    for item in right_column_content:
        if isinstance(item, Spacer):
            right_column.append([item])
        else:
            right_column.append([item])
    
    # Create data for main table
    table_data = []
    
    # Determine the max number of rows needed
    max_rows = max(len(left_column), len(right_column))
    
    # Fill in missing rows with empty strings
    while len(left_column) < max_rows:
        left_column.append([''])
    while len(right_column) < max_rows:
        right_column.append([''])
    
    # Create main table data
    for i in range(max_rows):
        table_data.append([left_column[i][0], right_column[i][0]])
    
    # Create the main table
    main_table = Table(table_data, colWidths=[left_col_width, right_col_width])
    main_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'LEFT'),
        ('LEFTPADDING', (0,0), (0,-1), 0),
        ('RIGHTPADDING', (0,0), (0,-1), 10),
        ('LEFTPADDING', (1,0), (1,-1), 10),
        ('RIGHTPADDING', (1,0), (1,-1), 0),
    ]))
    
    elements.append(main_table)
    
    # Declaration section
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph("<b>Declaration</b>", section_title_style))
    declaration_text = f"I, {data['name']}, hereby declare that all the information provided above are correct and complete to the best of my knowledge and belief. I understand that if any time it is found that any information given is false, my appointment is liable to be cancelled."
    elements.append(Paragraph(declaration_text, normal_style))
    
    # Signature line
    elements.append(Spacer(1, 0.3*inch))
    
    sig_data = [
        [Paragraph("_________________", normal_style), Paragraph(f"{data['city']}, {data['state']}", normal_style)],
        [Paragraph(data['name'], normal_style), ""]
    ]
    
    sig_table = Table(sig_data, colWidths=[3*inch, 3.5*inch])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
    ]))
    elements.append(sig_table)
    
    # Page number
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.drawRightString(
            7.5 * inch,
            0.25 * inch,
            f"1/1"
        )
        canvas.restoreState()
    
    # Build the PDF
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    
    # Reset the buffer position
    buffer.seek(0)
    
    return buffer
