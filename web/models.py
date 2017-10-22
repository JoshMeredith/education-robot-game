from sqlalchemy.ext.hybrid import hybrid_property

from web import bcrypt, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_id(self):
        return str(self.id)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codename = db.Column(db.String(64), unique=True, nullable=False)
    title = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Level %r: %r>' % (self.id, self.codename)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))

    code_score = db.Column(db.Integer)
    execution_score = db.Column(db.Integer)
