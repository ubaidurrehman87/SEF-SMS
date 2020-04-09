from django.urls import path

from . import views
urlpatterns = [
    path("", views.login, name="login"),
    path("index", views.index, name="index"),
    path("home/<str:name>",views.index1,name="home"),
    path("index-2 ",views.index2,name="index-2"),
    path("index-3 ",views.index2,name="index-3"),
    path("404-page",views.page_404,name="404-page"),
    path("500-page",views.page_505,name="500-page"),
    path("accordion",views.accordion,name="accordion"),
    
    # Student
    path("add-student/<str:name>",views.add_student ,name="add-student"),
    path("all-students",views.all_students ,name="all-students"),
    path("edit-student/<int:id>",views.edit_student,name="edit-student"),
    path("delete-student/<int:id>",views.delete_student ,name="delete-student"),
    path("student-csv/<str:name>",views.student_csv,name="student-csv"),
    path("student-profile/<int:id>",views.student_profile,name="student-profile"),
    path("student-pdf/<int:id>",views.student_pdf,name="student-pdf"),
    # Professor 
    path("add-professor/<str:name>",views.add_professor ,name="add-professor"),
    path("all-professors",views.all_professors ,name="all-professors"),
    path("delete-professor/<int:id>",views.delete_professor ,name="delete-professor"),
    path("edit-professor/<int:id>",views.edit_professor,name="edit-professor"),
    path("search-professor",views.search_professor ,name="search-professor"),
    path("professor-csv/<str:name>",views.professor_csv,name="professor-csv"),
    path("professor-profile/<int:id>",views.professor_profile,name="professor-profile"),
    
    # Other
    path("add-other/<str:name>",views.add_other ,name="add-other"),
    path("all-others",views.all_others ,name="all-others"),
    path("delete-other/<int:id>",views.delete_other ,name="delete-other"),
    path("edit-other/<int:id>",views.edit_other,name="edit-other"),
    path("search-other",views.search_other ,name="search-other"),
    path("other-csv/<str:name>",views.other_csv,name="other-csv"),
    path("other-profile/<int:id>",views.other_profile,name="other-profile"),

    # Class
    path("add-course/<str:name>",views.add_course,name="add-course"),
    path("all-courses",views.all_courses ,name="all-courses"),
    path("edit-course",views.edit_course,name="edit-course"),
    path("delete-course/<int:id>",views.delete_course ,name="delete-course"),

    # Subject
    path("add-subject/<str:name>",views.add_subject,name="add-subject"),
    path("all-subjects",views.all_subjects ,name="all-subjects"),
    
    # Salary
    path("add-salary/<str:name>",views.add_salary,name="add-salary"),
    path("all-salary",views.all_salary ,name="all-salary"),

     # Expenses
    path("add-expense/<str:name>",views.add_expense ,name="add-expense"),
    path("all-expenses",views.all_expenses ,name="all-expenses"),
    path("edit-expense/<int:id>",views.edit_expense,name="edit-expense"),
    path("table-expense/<int:id>",views.table_expense ,name="table-expense"),
    path("search-expense/<int:id>",views.search_expense ,name="search-expense"),
    
    # Salary Detail
    # path("professors-salary",views.professor_salary,name="professors-salary"),
    # path("others-salary",views.other_salary,name="others-salary"),
    # path("add-professor-salary/<str:name>",views.add_professor_salary,name="add-professor-salary"),
    # path("add-other-salary/<str:name>",views.add_other_salary,name="add-other-salary"),
    # path("edit-professor-salary/<int:id>",views.edit_professor_salary,name="edit-professor-salary"),
    # path("edit-other-salary/<int:id>",views.edit_other_salary,name="edit-other-salary"),
    # path("delete-professor-salary/<int:id>",views.delete_professor_salary,name="delete-professor-salary"),
    # path("delete-other-salary/<int:id>",views.delete_other_salary,name="delete-other-salary"),






    path("add-department",views.add_department ,name="add-department"),
    path("add-library-assets",views.add_library_assets ,name="add-library-assets"),
    path("advance-form-element",views.advance_form_element ,name="advance-form-element"),
    path("alerts",views.alerts ,name="alerts"),
    path("analytics",views.analytics ,name="analytics"),
    path("area-charts",views.area_charts ,name="area-charts"),
    path("bar-charts",views.bar_charts ,name="bar-charts"),
    path("basic-form-element",views.basic_form_element ,name="basic-form-element"),
    path("buttons",views.buttons ,name="buttons"),
    path("c3",views.c3,name="c3"),
    path("code-editor",views.code_editor,name="code-editor"),
    path("course-info",views.course_info,name="course-info"),
    path("course-payment",views.course_payment,name="course-payment"),
    path("course-profile",views.course_payment,name="course-profile"),
    path("search-courses",views.search_courses,name="search-courses"),
    path("data-maps",views.data_maps,name="data-maps"),
    path("data-table",views.data_table,name="data-table"),
    path("departments",views.departments,name="departments"),
    path("dual-list-box",views.dual_list_box,name="dual-list-box"),
    path("edit-department",views.edit_department,name="edit-department"),
    path("edit-library-assets",views.edit_library_assets,name="edit-library-assets"),
   
    
    path("events",views.events,name="events"),
    path("google-map",views.google_map,name="google-map"),
    path("images-cropper",views.images_cropper,name="images-cropper"),
    path("library-assets",views.library_assets,name="library-assets"),
    path("line-charts",views.line_charts,name="line-charts"),
    path("lock ",views.lock,name="lock"),
    # path("login ",views.login,name=" "),
    path("mailbox-compose",views.mailbox_compose,name="mailbox-compose"),
    path("mailbox-view",views.mailbox_view,name="mailbox-view"),
    path("mailbox",views.mailbox,name="mailbox"),
    path("modals",views.modals,name="modals"),
    path("multi-upload",views.multi_upload,name="multi-upload"),
    path("notifications",views.notifications,name="notifications"),
    path("password-meter",views.password_meter,name="password-meter"),
    path("password-recovery",views.password_recovery,name="password-recovery"),
    path("pdf-viewer",views.pdf_viewer,name="pdf-viewer"),
    path("peity",views.peity,name="peity"),
    path("preloader",views.preloader,name="preloader"),
    
    # path("register ",views.register,name=" "),
    path("rounded-chart",views.rounded_chart,name="rounded-chart"),
    path("sparkline",views.sparkline,name="sparkline"),
    path("static-table",views.static_table,name="static-table"),
    
    path("tabs",views.tabs,name="tabs"),
    path("tinymc",views.tinymc,name="tinymc"),
    path("tree-view",views.tree_view,name="tree-view"),
    path("widgets",views.widgets,name="widgets"),
    path("x-editable",views.x_editable,name="x-editable"),
    
    
    
    
    
]
