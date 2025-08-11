import pandas as pd
from django.core.management.base import BaseCommand
from courses.models import MITCourse, Quest, CapstoneProject

class Command(BaseCommand):
    help = 'Import MIT OCW courses from Excel file and seed Web Warrior data'

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

        # Seed Web Warrior Quests and Capstone
        quests_data = [
            {
                "title": "HTML Hero",
                "quest_number": 1,
                "difficulty": 1,
                "xp": 500,
                "icon": "📜",
                "story": "Begin your journey by forging the foundation of the web. Learn to craft the skeleton of every site.",
                "modules": [
                    "HTML Basics",
                    "Semantic Structure",
                    "Media & Links",
                    "Forms & Tables",
                    "Accessibility",
                ],
                "boss_battle": "Build a hero’s profile page with semantic HTML",
            },
            {
                "title": "CSS Conqueror",
                "quest_number": 2,
                "difficulty": 2,
                "xp": 600,
                "icon": "🎨",
                "story": "Gain the power to style your creations with elegance and adaptability.",
                "modules": [
                    "CSS Basics",
                    "Box Model & Layout",
                    "Typography",
                    "Animations",
                    "Responsive Design",
                ],
                "boss_battle": "Transform your HTML page into a responsive masterpiece",
            },
            {
                "title": "JavaScript Explorer",
                "quest_number": 3,
                "difficulty": 2,
                "xp": 700,
                "icon": "⚡",
                "story": "Bring life to your pages with interactivity and logic.",
                "modules": [
                    "JS Fundamentals",
                    "Logic & Functions",
                    "DOM Manipulation",
                    "Forms Validation",
                    "Debugging",
                ],
                "boss_battle": "Add dynamic features to your portfolio",
            },
            {
                "title": "DOM Defender",
                "quest_number": 4,
                "difficulty": 3,
                "xp": 800,
                "icon": "🛡",
                "story": "Master advanced DOM control and browser powers.",
                "modules": [
                    "Arrays & Objects",
                    "Advanced DOM",
                    "Browser APIs",
                    "ES6+ Features",
                    "Async Handling",
                ],
                "boss_battle": "To-do list app with Local Storage",
            },
            {
                "title": "Responsive Ranger",
                "quest_number": 5,
                "difficulty": 3,
                "xp": 900,
                "icon": "🏹",
                "story": "Create designs that adapt across all devices.",
                "modules": [
                    "Mobile-First Design",
                    "Flexbox",
                    "CSS Grid",
                    "Complex Layouts",
                    "Flex-Grid Combo",
                ],
                "boss_battle": "Responsive multi-section site",
            },
            {
                "title": "Framework Fighter (React)",
                "quest_number": 6,
                "difficulty": 4,
                "xp": 1000,
                "icon": "⚔",
                "story": "Wield React to build scalable apps.",
                "modules": [
                    "React Basics & JSX",
                    "Components & Props",
                    "State & Events",
                    "Conditional Rendering",
                    "Basic Hooks",
                ],
                "boss_battle": "Weather forecast app",
            },
            {
                "title": "API Adventurer",
                "quest_number": 7,
                "difficulty": 4,
                "xp": 1100,
                "icon": "📡",
                "story": "Harness API power for dynamic apps.",
                "modules": [
                    "REST API Basics",
                    "Fetching Data in React",
                    "Loading/Error States",
                    "Advanced Hooks",
                    "Deployment",
                ],
                "boss_battle": "Movie search app",
            },
            {
                "title": "Full-Stack Final Boss",
                "quest_number": 8,
                "difficulty": 5,
                "xp": 1500,
                "icon": "👑",
                "story": "Rule both frontend and backend realms.",
                "modules": [
                    "Node.js & Express",
                    "REST API",
                    "MongoDB",
                    "React+Backend Integration",
                    "Authentication & Security",
                ],
                "boss_battle": "Full-stack blog platform",
            },
        ]

        capstone = {
            "title": "Final Legendary Trial – Capstone Project",
            "xp": 3000,
            "icon": "🏆",
            "reward": "Web Warrior Badge",
            "objective": "Create and deploy a responsive, dynamic site with API integration and backend.",
        }

        for data in quests_data:
            Quest.objects.update_or_create(
                quest_number=data["quest_number"], defaults=data
            )

        CapstoneProject.objects.update_or_create(
            title=capstone["title"], defaults=capstone
        )

        self.stdout.write(self.style.SUCCESS('🏹 Seeded Web Warrior quests and capstone.'))
