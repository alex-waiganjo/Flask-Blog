from project import app
from project.routes import app
# from project import models
from project.models import db
db.init_app(app)

if __name__ == '__main__':
  app.run(debug=True)