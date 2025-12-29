from sqlalchemy.orm import Session


class AdminService():
    def __init__(self, session: Session):
        self.db = session
        
    def get_dashboard_data():
        ...