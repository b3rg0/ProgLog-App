"""empty message

Revision ID: 582315d9543d_
Revises: 
Create Date: 2018-11-13 21:32:26.287985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '582315d9543d_'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    subjects = op.create_table('subjects',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('date_created', sa.DateTime(), nullable=True),
        sa.Column('date_modified', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(length=120), nullable=False),
        sa.Column('prerequisite', sa.Integer(), nullable=False),
        sa.Column('minimum_approved', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    types = op.create_table('types',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('date_created', sa.DateTime(), nullable=True),
        sa.Column('date_modified', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    users = op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('date_created', sa.DateTime(), nullable=True),
        sa.Column('date_modified', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(length=150), nullable=False),
        sa.Column('email', sa.String(length=250), nullable=False),
        sa.Column('password', sa.String(length=250), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    nodes = op.create_table('nodes',
        sa.Column('id', sa.Integer(),  nullable=False),        
        sa.Column('subject_id', sa.Integer(), nullable=False),
        sa.Column('answer_parent', sa.String(length=250), nullable=False),
        sa.Column('parent_node', sa.Integer(), nullable=False),
        sa.Column('score', sa.Integer(), nullable=False),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('date_created', sa.DateTime(), nullable=True),
        sa.Column('date_modified', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
        sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
        sa.PrimaryKeyConstraint('id', 'subject_id')
    )
    user_subjects_rel = op.create_table('user_subjects_approved',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('subject_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'subject_id')
    )

    # Seeding database
    op.bulk_insert(subjects, [
        {'name': 'Variables', 'minimum_approved': 15, 'prerequisite': 0},
        {'name': 'Estructuras de Control', 'minimum_approved': 15, 'prerequisite': 1},
        {'name': 'Bucles', 'minimum_approved': 15, 'prerequisite': 2},
        {'name': 'Arreglos', 'minimum_approved': 15, 'prerequisite': 3},                                
        {'name': 'Metodos', 'minimum_approved': 15, 'prerequisite': 4},
        {'name': 'Apuntadores', 'minimum_approved': 15, 'prerequisite': 5},
    ])

    op.bulk_insert(types, [
        {'name': 'Correcta'},
        {'name': 'Incorrecta'},
    ])

    op.bulk_insert(nodes, [
                                ###Variables
        ### cpp1
        {'id': 1, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'None', 'parent_node': 0},
        {'id': 2, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 15', 'parent_node': 1},
        {'id': 3, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'15\'', 'parent_node': 1},
        {'id': 4, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'Error', 'parent_node': 1},

        ### cpp2
        {'id': 5, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 15', 'parent_node': 2},
        {'id': 6, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'50\'', 'parent_node': 2},
        {'id': 7, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 50', 'parent_node': 2},

        ### cpp3
        {'id': 8, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 12', 'parent_node': 3},
        {'id': 9, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'12\'', 'parent_node': 3},
        {'id': 10, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 7', 'parent_node': 3},

        ### cpp4
        {'id': 11, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 10', 'parent_node': 4},
        {'id': 12, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'Error', 'parent_node': 4},
        {'id': 13, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'a\'', 'parent_node': 4},

        ### cpp5
        {'id': 14, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'True\'', 'parent_node': 5},
        {'id': 15, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 5', 'parent_node': 5},
        {'id': 16, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = -5', 'parent_node': 5},

        ### cpp6
        {'id': 17, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = \'Error\'', 'parent_node': 6},
        {'id': 18, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 0', 'parent_node': 6},
        {'id': 19, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'0\'', 'parent_node': 6},

        ### cpp7
        {'id': 20, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'Error\'', 'parent_node': 7},
        {'id': 21, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 150', 'parent_node': 7},
        {'id': 22, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 60', 'parent_node': 7},

        ### cpp8
        {'id': 23, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 10', 'parent_node': 8},
        {'id': 24, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 100', 'parent_node': 8},
        {'id': 25, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'10\'', 'parent_node': 8},

        ### los nodos 9, 10, 12 y 13 ya dan -10 por ende game over, para no perder el hilo le puse el num 11 al que sigue

        ### cpp11
        {'id': 26, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 55', 'parent_node': 11},
        {'id': 27, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 5', 'parent_node': 11},
        {'id': 28, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 100', 'parent_node': 11},

        ### cpp15
        {'id': 29, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 4', 'parent_node': 15},
        {'id': 30, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = -5', 'parent_node': 15},
        {'id': 31, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 1', 'parent_node': 15},

        ### cpp17
        {'id': 32, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 5', 'parent_node': 17},
        {'id': 33, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 2', 'parent_node': 17},
        {'id': 34, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 15', 'parent_node': 17},

        ### cpp24
        {'id': 35, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 20', 'parent_node': 24},
        {'id': 36, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 1', 'parent_node': 24},
        {'id': 37, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 30', 'parent_node': 24},

        ### cpp27
        {'id': 38, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 200', 'parent_node': 27},
        {'id': 39, 'subject_id': 1, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 12', 'parent_node': 27},
        {'id': 40, 'subject_id': 1, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 3', 'parent_node': 27},

        ## la repesca es para que saquen 15 sino se jodieron

                                ###Estructuras de Control

        ### cpp1
        {'id': 1,'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'None', 'parent_node': 0},
        {'id': 2, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 4', 'parent_node': 1},
        {'id': 3, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 15', 'parent_node': 1},
        {'id': 4, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 12', 'parent_node': 1},

        ### cpp2
        {'id': 5, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'x = 0', 'parent_node': 2},
        {'id': 6, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 10', 'parent_node': 2},
        {'id': 7, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': '\'Error\'', 'parent_node': 2},

        ### cpp3
        {'id': 8, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 12', 'parent_node': 3},
        {'id': 9, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': '\'Error\'', 'parent_node': 3},
        {'id': 10, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 4', 'parent_node': 3},

        ### cpp4
        {'id': 11, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 10', 'parent_node': 4},
        {'id': 12, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 11', 'parent_node': 4},
        {'id': 13, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'a\'', 'parent_node': 4},

        ### cpp5
        {'id': 14, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 2', 'parent_node': 5},
        {'id': 15, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 15', 'parent_node': 5},
        {'id': 16, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 50', 'parent_node': 5},

        ### cpp6
        {'id': 17, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 11', 'parent_node': 6},
        {'id': 18, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 12', 'parent_node': 6},
        {'id': 19, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = \'11\'', 'parent_node': 6},

        ### cpp7
        {'id': 20, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'a = 15', 'parent_node': 7},
        {'id': 21, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 2', 'parent_node': 7},
        {'id': 22, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 12', 'parent_node': 7},

        ### cpp8
        {'id': 23, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 75', 'parent_node': 8},
        {'id': 24, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 25', 'parent_node': 8},
        {'id': 25, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 5', 'parent_node': 8},

        ### cpp11
        {'id': 26, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 225', 'parent_node': 11},
        {'id': 27, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 50', 'parent_node': 11},
        {'id': 28, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 15', 'parent_node': 11},

        ### cpp15
        {'id': 29, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 2', 'parent_node': 15},
        {'id': 30, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 3', 'parent_node': 15},
        {'id': 31, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 1', 'parent_node': 15},

        ### cpp17
        {'id': 32, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 1', 'parent_node': 17},
        {'id': 33, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'c = 2', 'parent_node': 17},
        {'id': 34, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 3', 'parent_node': 17},

        ### cpp24
        {'id': 35, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'd = 3', 'parent_node': 24},
        {'id': 36, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'd = 5', 'parent_node': 24},
        {'id': 37, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'd = 4', 'parent_node': 24},

        ### cpp27
        {'id': 38, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 200', 'parent_node': 27},
        {'id': 39, 'subject_id': 2, 'type_id': 1, 'score': 10, 'answer_parent': 'd = 12', 'parent_node': 27},
        {'id': 40, 'subject_id': 2, 'type_id': 2, 'score': -5, 'answer_parent': 'c = 3', 'parent_node': 27},

                                ###Bucles 

        ### cpp1
        {'id': 1, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'None', 'parent_node': 0},
        {'id': 2, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 6', 'parent_node': 1},
        {'id': 3, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 5', 'parent_node': 1},
        {'id': 4, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 1', 'parent_node': 1},

        ### cpp2
        {'id': 5, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 2', 'parent_node': 2},
        {'id': 6, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 1', 'parent_node': 2},
        {'id': 7, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 3', 'parent_node': 2},

        ### cpp3
        {'id': 8, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent':  'a = 5', 'parent_node': 3},
        {'id': 9, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent':  '\'Error\'', 'parent_node': 3},
        {'id': 10, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 0', 'parent_node': 3},

        ### cpp4
        {'id': 11, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 0', 'parent_node': 4},
        {'id': 12, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 1', 'parent_node': 4},
        {'id': 13, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 5', 'parent_node': 4},

        ### cpp5
        {'id': 14, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 0', 'parent_node': 5},
        {'id': 15, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'a = 4', 'parent_node': 5},
        {'id': 16, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'a = 5', 'parent_node': 5},        

        ### cpp6
        {'id': 17, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 3', 'parent_node': 6},
        {'id': 18, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 2', 'parent_node': 6},
        {'id': 19, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 4', 'parent_node': 6},

        ### cpp7
        {'id': 20, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 3', 'parent_node': 7},
        {'id': 21, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 5', 'parent_node': 7},
        {'id': 22, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 4', 'parent_node': 7},

        ### cpp8
        {'id': 23, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 10', 'parent_node': 8},
        {'id': 24, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'b = 0', 'parent_node': 8},
        {'id': 25, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'se genera un bucle infinito', 'parent_node': 8},

        ### cpp11
        {'id': 26, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 20', 'parent_node': 11},
        {'id': 27, 'subject_id': 3, 'type_id': 1, 'score': 10, 'answer_parent': 'se genera un bucle infinito', 'parent_node': 11},
        {'id': 28, 'subject_id': 3, 'type_id': 2, 'score': -5, 'answer_parent': 'b = 10', 'parent_node': 11},


    ])


    "op.bulk_insert()"
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_subjects_approved')
    op.drop_table('nodes')
    op.drop_table('users')
    op.drop_table('types')
    op.drop_table('subjects')
    # ### end Alembic commands ###
