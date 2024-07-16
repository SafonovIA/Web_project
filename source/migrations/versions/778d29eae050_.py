"""empty message

Revision ID: 778d29eae050
Revises: 440a01684836
Create Date: 2024-07-16 03:01:56.221636

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '778d29eae050'
down_revision = '440a01684836'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accessories', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('outwears', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('shoes', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('socks', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('sweatwears', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('trousers', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('tshirts', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               type_=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('city')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.TEXT(), autoincrement=False, nullable=False))

    with op.batch_alter_table('tshirts', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    with op.batch_alter_table('trousers', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    with op.batch_alter_table('sweatwears', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    with op.batch_alter_table('socks', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    with op.batch_alter_table('shoes', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    with op.batch_alter_table('outwears', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    with op.batch_alter_table('accessories', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.Enum('мужской', 'женский', 'детский', name='gender_enum', schema='public'),
               type_=postgresql.ENUM('мужской', 'женский', 'детский', name='gender_enum'),
               existing_nullable=False)

    # ### end Alembic commands ###