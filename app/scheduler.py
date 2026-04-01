from apscheduler.schedulers.background import BackgroundScheduler
from app.service import update_cars
from app.config import UPDATE_INTERVAL_HOURS

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_cars, "interval", hours=UPDATE_INTERVAL_HOURS)
    scheduler.start()