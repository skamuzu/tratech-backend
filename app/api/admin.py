from app.services.admin import get_dashboard_service
from fastapi import APIRouter, Depends
from app.schemas.admin import DashboardData

router = APIRouter(prefix="/admin")
@router.get("/dashboard", response_model=DashboardData)
def get_dashboard_data(dashboard_service=Depends(get_dashboard_service)):
    data = dashboard_service.get_dashboard_data()
    return data