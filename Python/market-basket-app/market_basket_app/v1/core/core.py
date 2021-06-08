from sqlalchemy import \
    create_engine, MetaData, Column, Table, Integer, String, Float, select

DB_URL = 'sqlite:///../data/market_basket.db'

engine = create_engine(DB_URL)

metadata = MetaData(bind=engine)

market_basket_table = Table(
    'market_basket_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('market', String(50), nullable=False),
    Column('product', String(50), nullable=False),
    Column('price', Float, nullable=False),
    Column('quantity', String(25), nullable=False))

metadata.create_all()
