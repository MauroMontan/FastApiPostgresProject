



#this function is for create a new recording
def add_row(model, db):
    db.add(model)
    db.commit()
    db.refresh(model)
