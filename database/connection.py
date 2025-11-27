from sqlmodel import SQLModel, Session, create_engine

# Настройки базы данных
database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}

# Создаем движок базы данных
engine = create_engine(
    database_connection_string, 
    echo=True,  # Показывает SQL запросы в консоли
    connect_args=connect_args
)

def create_db_and_tables():
    """Создает базу данных и таблицы при запуске приложения"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Генератор сессий для работы с базой данных"""
    with Session(engine) as session:
        yield session