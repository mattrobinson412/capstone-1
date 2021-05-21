# CAPSTONE 1 **PROPOSAL**

***Application for The Expositors Seminary:***

1. This application will serve as a platform for alumni and current students to gather resources, find churches within the network of graduates and affiliated ministries, for admin to add new resources as they are produced, and for donors to give to the seminary for the furthering of the cause in the community.
2. The user demographics are:
    1. Active Students,
        1. Gender: M,
        2. Range: 21-70,
        3. Avg: 30-40
    2. Former Students (Alumni),
        1. Gender: M,
        2. Range: 30-80,
        3. Avg: 40-50
    3. Donors,
        1. Gender: M + F,
        2. Range: 35-70,
        3. Avg: 50-60
    4. Admin,
        1. Gender: M,
        2. Range: 30-60,
        3. Avg: 45.
3. The data will be drawn from:
    1. Vimeo (the TES account),
    2. Square (?) (the TES account),
    3. Google Maps (for church-finding).
4. The outline of the project creation process is this:
    1. The database schema will consist of these tables:
        1. A ‘User’ table,
            1. Id,
            2. First_name,
            3. Last_name,
            4. password,
            5. Phone_number,
            6. Email,
            7. Status_id (fk referencing ‘Status’ column ‘status’),
            8. Donor_id (nullable = True).
        2. A ‘Status’ table (i.e. student, alumni, etc.),
            1. Status_id,
            2. Status.
        3. A ‘Donations’ table,
            1. User_id (fk referencing ‘User’ column ‘id’),
            2. Date,
            3. Amount,
            4. Payment_type.
        4. A ‘Classes’ table,
            1. id,
            2. Name,
            3. Date,
            4. Professor.
        5. A ‘Lectures’ table,
            1. Class_id (fk referencing ‘Classes’ column ‘id’),
            2. Name (?),
            3. Link,
            4. Date,
            5. Duration.
        6. A ‘Syllabi’ table,
            1. Class_id (fk referencing ‘Classes’ column ‘id’),
            2. Name,
            3. Link.
        7. A ‘Documents’ table,
            1. Class_id (fk referencing ‘Classes’ column ‘id’),
            2. Name,
            3. Link.
        8. A ‘Churches’ table,
            1. Id,
            2. Name,
            3. Location,
            4. Phone Number,
            5. Email,
            6. Website.
        9. A ‘Graduates’ table,
            1. Id,
            2. First_name,
            3. Last_name,
            4. Class,
            5. Church_id (fk referencing “Churches’ column ‘id’),
            6. Role.
        10. A ‘Resources’ table,
    2. The back-end portion will cover 3 components:
        1. A RESTful API,
            1. **GET**:
                1. Classes,
                    1. Lectures,
                    2. Syllabi,
                    3. Documents.
                2. Churches,
                    1. Campus churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                    2. Graduate churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                        3. Role of graduate.
                    3. Resources,
                        1. Chapel sermons,
                        2. Blog posts,
                        3. TES updates (?).
            2. **POST**:
                1. Classes,
                    1. Lectures,
                    2. Syllabi,
                    3. Documents.
                2. Churches,
                    1. Campus churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                    2. Graduate churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                        3. Role of graduate.
                3. Resources,
                    1. Chapel sermons,
                    2. Blog posts,
                    3. TES updates (?).
            3. **PUT**:
                1. Classes,
                    1. Lectures,
                    2. Syllabi,
                    3. Documents.
                2. Churches,
                    1. Campus churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                    2. Graduate churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                        3. Role of graduate.
                3. Resources,
                    1. Chapel sermons,
                    2. Blog posts,
                    3. TES updates (?).
            4. **PATCH**:
                1. Classes,
                    1. Lectures,
                    2. Syllabi,
                    3. Documents.
                2. Churches,
                    1. Campus churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                    2. Graduate churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                        3. Role of graduate.
                3. Resources,
                    1. Chapel sermons,
                    2. Blog posts,
                    3. TES updates (?).
            5. **DELETE**:
                1. Classes,
                    1. Lectures,
                    2. Syllabi,
                    3. Documents.
                2. Churches,
                    1. Campus churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                    2. Graduate churches,
                        1. Location,
                        2. Contact info,
                            1. Phone Number,
                            2. Email,
                            3. Website.
                        3. Role of graduate.
                3. Resources,
                    1. Chapel sermons,
                    2. Blog posts,
                    3. TES updates (?).
        2. Flask Blueprint routing,
            1. “/”,
                1. Initial home page for site.
            2. ‘/login’
                1. Where users with accounts can login.
            3. ‘/register’
                1. Where unregistered users can sign up for access.
            4. ‘/churches’
                1. Where users can find campus churches and graduate churches across the globe.
            5. ‘/resources’
                1. Where users can access public resources from the TES admin and faculty.
            6. ‘/contact’
                1. Where users can contact the admin team and also inquire about gaining greater access to the app.
            7. ‘/<user_id>/home’
                1. Where logged-in users can see their dashboard and relevant portals.
            8. ‘/<user_id>/donate’
                1. Where logged-in users can donate securely to TES.
            9. ‘/<user_id>/classes’
                1. Where logged-in users can view the catalog of classes.
            10. ‘/<user_id>/classes/<class_id>’
                1. Where logged-in users can view everything pertaining to one specific class.
            11. ‘/<user_id>/classes/<class_id>/lectures’
                1. Where logged-in users can view the catalog of lectures pertaining to one specific class.
            12. ‘/<user_id>/classes/<class_id>/lectures/<lecture_id>’
                1. Where logged-in users can access a single specific lecture pertaining to one specific class.
            13. ‘/<user_id>/classes/<class_id>/syllabi’
                1. Where logged-in users can view the syllabi pertaining to one specific class.
            14. ‘/<user_id>/classes/<class_id>/syllabi/<syllabi_id>’
                1. Where logged-in users can access a single specific syllabus pertaining to one specific class.
            15. ‘/<user_id>/classes/<class_id>/documents’
                1. Where logged-in users can view the documents pertaining to one specific class.
            16. ‘/<user_id>/classes/<class_id>/documents/<document_id>’
                1. Where logged-in users can access a single specific document pertaining to one specific class.
        3. Flask-SQLAlchemy modeling,
            1. There will be models for every table mentioned in Section I,
                1. Each will access the respective API’s needed to produce the information desired for its function.