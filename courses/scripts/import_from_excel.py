import pandas as pd
from courses.models import MITCourse

def import_ocw_courses(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        title = row.get('Title') or 'Untitled'
        subject = row.get('Subject') or 'General'
        url = row.get('Link') or ''
        description = row.get('Description') or ''
        thumbnail = row.get('Thumbnail') or ''

        if url:
            MITCourse.objects.get_or_create(
                url=url,
                defaults={
                    'title': title,
                    'subject': subject,
                    'description': description,
                    'thumbnail': thumbnail
                }
            )
