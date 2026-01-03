from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random
import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
# db_path = os.path.join(BASE_DIR, "cafes.db")

app = Flask(__name__)

# Ensure instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# Build DB path inside instance/
db_path = os.path.join(app.instance_path, "cafes.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"



# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
            #Method 1. 
            # dictionary = {}
            # # Loop through each column in the data record
            # for column in self.__table__.columns:
            #     #Create a new dictionary entry;
            #     # where the key is the name of the column
            #     # and the value is the value of the column
            #     dictionary[column.name] = getattr(self, column.name)
            # return dictionary
            
            #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
            return {column.name: getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()

with app.app_context():   #debugging
    print("USING DB:", db.engine.url.database)
    
with app.app_context():  #debugging
    db_file = db.engine.url.database
    print("USING DB:", db_file)
    print("DB FILE EXISTS:", os.path.exists(db_file))
    print("DB FILE SIZE:", os.path.getsize(db_file))



    
@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def all_cafes():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    cafes = result.scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        error_msg = {
            "error": {"Not found": f"Sorry, we didn't find {query_location}"}
        }
        return jsonify(error_msg), 404
    
# @app.route("/add", methods=["POST"])
# def post_new_cafe():
#     data = request.form if request.form else request.args
#     print("CONTENT-TYPE:", request.content_type)
#     print("FORM:", request.form.to_dict())
#     print("JSON:", request.get_json(silent=True))

#     new_cafe = Cafe(
#         name=request.form.get("name"),
#         map_url=request.form.get("map_url"),
#         img_url=request.form.get("img_url"),
#         location=request.form.get("loc"),
#         has_sockets=bool(request.form.get("sockets")),
#         has_toilet=bool(request.form.get("toilet")),
#         has_wifi=bool(request.form.get("wifi")),
#         can_take_calls=bool(request.form.get("calls")),
#         seats=request.form.get("seats"),
#         coffee_price=request.form.get("coffee_price"),
#     )
#     db.session.add(new_cafe)
#     db.session.commit()
#     return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/add", methods=["POST"])
def post_new_cafe():
    data = request.form if request.form else request.args  # <-- key line

    new_cafe = Cafe(
        name=data.get("name"),
        map_url=data.get("map_url"),
        img_url=data.get("img_url"),
        location=data.get("loc"),
        has_sockets=bool(data.get("sockets")),
        has_toilet=bool(data.get("toilet")),
        has_wifi=bool(data.get("wifi")),
        can_take_calls=bool(data.get("calls")),
        seats=data.get("seats"),
        coffee_price=data.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(entity=Cafe, ident=cafe_id)  # Returns None if cafe_id is not found
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.get(Cafe, cafe_id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

@app.route("/debug/locations")
def debug_locations():
    result = db.session.execute(db.select(Cafe.location))
    return jsonify(locations=[repr(loc) for loc in result.scalars().all()])

@app.route("/debug/count")
def debug_count():
    return {"count": db.session.query(Cafe).count()}



    


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
