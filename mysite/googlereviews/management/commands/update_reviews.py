import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from googlereviews.models import GoogleReview


class Command(BaseCommand):
    help = "Fetch Google reviews from FastAPI and store them in the database"

    def handle(self, *args, **kwargs):
        business_url = "https://maps.app.goo.gl/R4bjzYGUps4KeRQV7"
        api_url = "http://195.110.58.9:8069/google_reviews"
        api_token = "3RAwR0?hap!odRasw_?$"

        payload = {"url": business_url, "max_page": 2}

        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        try:
            response = requests.post(api_url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            reviews = response.json()

            if not isinstance(reviews, list):
                self.stdout.write(self.style.ERROR("Unexpected response format"))
                return

            for r in reviews:
                date_str = r.get("date")
                parsed_date = None
                if date_str:
                    try:
                        parsed_date = datetime.fromisoformat(date_str).date()
                    except ValueError:
                        self.stdout.write(
                            self.style.ERROR(f"Invalid date format: {date_str}")
                        )
                        continue

                GoogleReview.objects.update_or_create(
                    review_id=r.get("review_id"),
                    defaults={
                        "author": r.get("author"),
                        "profile_picture": r.get("profile_picture"),
                        "date": parsed_date,
                        "rating": r.get("rating"),
                        "body": r.get("body"),
                    },
                )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully updated {len(reviews)} reviews.")
            )

        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Failed to fetch from API: {str(e)}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Unexpected error: {str(e)}"))
