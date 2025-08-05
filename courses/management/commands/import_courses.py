import pandas as pd
from django.core.management.base import BaseCommand
from courses.models import MITCourse

class Command(BaseCommand):
    help = 'Import MIT OCW courses from Excel file'

    def handle(self, *args, **kwargs):
        file_path = 'courses/data/mit_ocw_courses.xlsx'  # Update this path if needed

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading file: {e}'))
            return

        count = 0

        for _, row in df.iterrows():
            title = row.get('Title') or 'Untitled'
            subject = row.get('Subject') or 'General'
            url = row.get('Link') or ''
            description = row.get('Description') or ''
            thumbnail = row.get('Thumbnail') or ''

            if url:
                _, created = MITCourse.objects.get_or_create(
                    url=url,
                    defaults={
                        'title': title,
                        'subject': subject,
                        'description': description,
                        'thumbnail': thumbnail
                    }
                )
                if created:
                    count += 1

        self.stdout.write(self.style.SUCCESS(f'✅ Imported {count} new courses successfully!'))
