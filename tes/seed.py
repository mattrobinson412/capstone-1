from models import *

def load_test_data(db):
    db.drop_all()
    db.create_all()

    User.query.delete()
    Status.query.delete()
    Donation.query.delete()
    Class.query.delete()
    Lecture.query.delete()
    Syllabus.query.delete()
    Document.query.delete()
    Church.query.delete()
    Graduate.query.delete()
    Staff.query.delete()
    Resource.query.delete()
    Contact.query.delete()

    admin = Status(status="Admin")
    alum = Status(status="Alumni")
    student = Status(status="Student")
    donor = Status(status="Donor")

    db.session.add(admin)
    db.session.add(alum)
    db.session.add(student)
    db.session.add(donor)
    db.session.commit()

    m = User(first_name="Matt",
                    last_name="Robinson",
                    password="mattydimes",
                    phone_number="239-249-9208",
                    email="fake@gmail.com",
                    status_id=3)

    d = User(first_name="Dan",
                    last_name="Ha-Adam",
                    password="wisconsin",
                    phone_number="561-165-5611",
                    email="real@gmail.com",
                    status_id=1)

    dar = User(first_name="Da'Ron",
                    last_name="Roberts",
                    password="katyperrybible",
                    phone_number="732-237-7322",
                    email="maybe@gmail.com",
                    status_id=2)

    # bobby = User(first_name="Bob",
    #             last_name="V",
    #             password="techlyfe",
    #             phone_number="515-515-5151",
    #             email="kinda@gmail.com",
    #             status=4)

    matty = m.register(m.first_name,
                        m.last_name,
                        m.password,
                        m.phone_number,
                        m.email,
                        m.status_id)
    
    db.session.add(matty)

    dan = d.register(d.first_name,
                        d.last_name,
                        d.password,
                        d.phone_number,
                        d.email,
                        d.status_id)
    
    db.session.add(dan)

    daron = dar.register(dar.first_name,
                        dar.last_name,
                        dar.password,
                        dar.phone_number,
                        dar.email,
                        dar.status_id)

    db.session.add(daron)

    # bob = b.register(bobby.first_name,
    #                     bobby.password,
    #                     bobby.phone_number,
    #                     bobby.email)

    db.session.commit()

    donation = Donation(user_id=3,
                        first_name="Matt",
                        last_name="Robinson",
                        date="8/9/2020",
                        amount=550.00,
                        payment_type="credit")

    db.session.add(donation)
    db.session.commit()

    gibc = Church(name="Grace Immanuel Bible Church",
                    location="Jupiter, FL",
                    phone_number="561-561-5615",
                    email="church@gmail.com",
                    website="www.gibcjupiter.org")

    db.session.add(gibc)
    db.session.commit()

    grad = Graduate(first_name="Brian",
                    last_name="Arnold",
                    grad_year="2012",
                    church_id=1,
                    role="Youth Pastor")

    db.session.add(grad)
    db.session.commit()

    matty_dubs = Staff(first_name="Matt",
                        last_name="Waymeyer",
                        join_date="7/6/2012",
                        church_id=1,
                        role="Professor")

    db.session.add(matty_dubs)
    db.session.commit()

    res = Resource(title="The First Resurrection and Revelation 20",
                    link="https://www.tms.edu/m/TMS-Spring2016-Article-01.pdf",
                    category="Journal",
                    staff_id=1)

    db.session.add(res)
    db.session.commit()

    greek = Class(name="Greek I",
                    date="Fall 2020",
                    staff_id=1)

    db.session.add(greek)
    db.session.commit()


    lecture = Lecture(class_id=1,
                        name="Intro Lecture",
                        link="https://vimeo.com/560052457",
                        date="08/09/21",
                        staff_id=1)

    db.session.add(lecture)
    db.session.commit()

    syl = Syllabus(class_id=1,
                    name="Greek I Syllabus",
                    link="file:///C:/Users/12392/Downloads/NT503%20Syllabus%20(2).pdf")
    
    db.session.add(syl)
    db.session.commit()

    doc = Document(class_id=1,
                    name="Basics of Line Diagramming",
                    link="file:///C:/Users/12392/Downloads/Basics%20of%20Line%20Diagramming%20(Part%201).pdf")

    db.session.add(doc)
    db.session.commit()

    contact = Contact(first_name="AJ",
                        last_name="Caldwell",
                        email="stud@gmail.com",
                        message="Let me into Expositors, man!")

    db.session.add(contact)
    db.session.commit()
            