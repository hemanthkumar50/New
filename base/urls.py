from django.urls import path
from LMS import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView

from .Routes.common import *
from .Routes.Common_Tool import *
from .Routes.tool import *
from .Routes.staff import *
from .Routes.students import *
from .Routes.study import *
from .Routes.notes import *
from .Routes.exam import *
from .Routes.blog import *
from .Routes.Events import *
from .Routes.home import *
from .Routes.CommonNotes import *
from .Routes.DynamicFunctionality import *
from .Routes.admin_page import *
from .Routes.staff_tools import *


# Initilizes........................

urlpatterns = []


def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets

# Urls............................


tools = [
    path('Common_tool', Common_tool),
    path('toolHome', toolHome),
    path('trans', translate_, name='trans'),
    path('convert_text', convert_text, name='convert_text'),
    path('wikipedia_summary', wikipedia_summary, name='wikipedia_summary'),
    path('convert_docx_to_pdf', convert_docx_to_pdf),
    path('convert_pdf_to_docx', convert_pdf_to_docx,name='convert_pdf_to_docx'),
    path('convert_pdf_to_excel', convert_pdf_to_excel,name='convert_pdf_to_excel'),
    path('convert_excel_to_pdf', convert_excel_to_pdf,name='convert_excel_to_pdf'),
    path('convert_jpg_to_pdf', convert_jpg_to_pdf,name='convert_jpg_to_pdf'),
    path('convert_jpg_to_word', convert_jpg_to_word,name='convert_jpg_to_word'),
    path('calculator', calculator,name='calculator'),
    path('cgpa_calculator', cgpa_calculator),
    path('handwriting_converter', handwriting_converter,
         name='handwriting_converter'),
    path('keyword_to_image', keyword_to_image, name='keyword_to_image'),
    path('video_meeting/<str:room_id>', meeting, name='video_meeting'),
    path('staff_meeting/<str:room_id>', staff_meeting, name='staff_meeting'),
    path('join_meeting', join_meeting, name='join_meeting'),
    path('staff_join_meeting', staff_join_meeting, name='staff_join_meeting'),

    path('gpa_calculator', gpa_calculator, name='gpa_calculator'),
    path('get_subject', get_subject),
    path('Code_scriping', Code_scriping, name='Code_scriping'),
]
alternative_url = [path('student/video_meeting', meeting),
                   path('student/class_room', home_classroom),
                   path('student/chat_lobby', lobby),
                   path('student/list_blog', student_list_blog),
                   path('student/chat_home/', chat_home, name='chat_home'),
                   path('student/note/notes_list',
                        notes_list, name='notes_list'),
                   path('student/note/std/notes_list',
                        student_notes_list, name='student_notes_list'),
                   path('staff/note/std/notes_list',
                        staff_notes_list, name='staff_notes_list'),
                   path('student/toolHome', toolHome, name='toolHome'),
                   path('student/logout', LogoutView.as_view)

                   ]

common_tool = [
    path('Common_Common_tool', Common_Common_tool),
    path('Common_toolHome', Common_toolHome),
    path('Common_trans', Common_translate_),
    path('Common_convert_text', Common_convert_text),
    path('Common_wikipedia_summary', Common_wikipedia_summary),
    path('Common_convert_docx_to_pdf', Common_convert_docx_to_pdf),
    path('Common_convert_pdf_to_docx', Common_convert_pdf_to_docx),
    path('Common_convert_pdf_to_excel', Common_convert_pdf_to_excel),
    path('Common_convert_excel_to_pdf', Common_convert_excel_to_pdf),
    path('Common_convert_jpg_to_pdf', Common_convert_jpg_to_pdf),
    path('Common_convert_jpg_to_word', Common_convert_jpg_to_word),
    path('Common_calculator', Common_calculator),
    path('Common_cgpa_calculator', Common_cgpa_calculator),
    path('Common_handwriting_converter', Common_handwriting_converter),
    path('Common_keyword_to_image', Common_keyword_to_image),
    path('Common_video_meeting', Common_video_meeting),

    path('Common_gpa_calculator', Common_gpa_calculator),
    path('Common_get_subject', Common_get_subject),
    path('Common_Code_scriping', Common_Code_scriping),
]

common = [
    path('', pre_home),
    path('pre_home', pre_home),
    path('student_home', student_home, name='student_home'),
    path('staff_home', staff_home, name='staff_home'),
    path('contactus', contactus),
    path('services', services),
    path('about', about),
    path('personal_detials', Personal_detials, name='personal_detials'),
]

admin = [
    path('add_Faculty', add_faculty),
    path('teacher_list', teacher_list, name='teacher_list'),
    path('teacher_delete/<str:teacher_id>',
         teacher_delete, name='teacher_delete'),
    path('teacher_edit/<str:teacher_id>', teacher_edit, name='teacher_edit'),
    path('add_usr', add_usr),
    path('teachers', teachers),
    path('teachers/profile/<int:pk>/', teacher_profile, name='teacher_profile'),
    path('class_list', class_list, name='class_list'),
    path('class_listout/<str:class_id>',
         get_class_peoples, name='class_listout'),
    path('students_list', students_list, name='students_list'),
    path('admin_students_list', admin_students_list, name='admin_students_list'),
    path('students_list_by_dep', students_list_by_dep,
         name='students_list_by_dep'),
    path('class_dates', class_dates, name='class_dates'),
    path('class_dates/data/<str:class_id>/<str:date>/',
         export_attendees, name='export_attendees'),
    path('class_dates/<int:id>/delete_attendee/',
         delete_attendee, name='delete_attendee'),
    path('class_dates/<int:id>/edit_attendee/',
         edit_attendee, name='edit_attendee'),
    path('class_dates/<str:class_id>/<str:date>/user_details/',
         user_details, name='user_details'),
]


videochat = [
    path('chat_lobby', lobby),
    path('room/', video_chat_room),
    path('get_token/', getToken),

    path('create_member/', createMember),
    path('get_member/', getMember),
    path('delete_member/', deleteMember),
]


chatroom = [
    path('chat_home/', chat_home, name='chat_home'),
    path('staff_chat_home/', staff_chat_home, name='staff_chat_home'),
    # problem...................
    path('chat/<str:room>/', chat_room, name="chat_room"),
    path('staffchat/<str:room>/', staff_chat_room, name="staff_chat_room"),
    path('chat_home/checkview', checkview, name="checkview"),
    path('chat_home/staff_checkview', staff_checkview, name="staff_checkview"),
    path('chat_home/Ncheckview', Ncheckview, name="Ncheckview"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),
]


classroom = [
    path('test_marks/<str:class_id>/', test_marks, name='test_marks'),
    path('add_test_marks/<str:class_id>',
         add_test_marks, name='add_test_marks'),
    path('edit_test_marks/<str:class_id>/<str:sub>/<int:ass_no>',
         edit_test_marks, name='edit_test_marks'),
    path('class_room', home_classroom, name='class_room'),
    path('message/<str:room>/', chatgetMessages, name="message"),
    path('classroom/<str:pk>/<str:class_id>', nave_home_classroom),
    path('add_class', add_class),
    path('delete_class/<str:room>', delete_class),
    path("save_added_class", save_add_class),
    path("edit_classroom/<str:classroom_id>", edit_classroom),
    path("attendes", attendes),
    path("update_attendes", update_attendes),
    path("update_edited_attendes", update_edited_attendes),
    path("edit_attendes_home", edit_attendes_home),
    path("view_attendes", view_attendes),
    path("edit_attendes", edit_attendes),
    path("mark/<str:class_id>", mark),
    path("update_marks", update_mark),
    path("edit_mark_home", edit_mark_home),
    path("edit_mark", edit_mark),
    path("update_edited_mark", update_edited_mark),
    path("marks_by_class/<str:class_id>", marks_by_class),
    path("add_class_notes/<str:pk>", add_class_notes),
    path('class_ebook/book_list', class_book_list, name='class_book_list'),
    path('class_ebook/<int:pk>/edit/', class_ebook_edit, name='class_ebook_edit'),
    path('class_ebook/<int:pk>/delete/',
         class_ebook_delete, name='class_ebook_delete'),

]


studet = [
    path('students_list', students_list, name='students_list'),
    path('students/<int:student_id>', student_profile, name='student_detail'),
    path('students_delete/<int:student_id>/delete',
         student_delete, name='student_delete'),

    path('student/<int:pk>/edit', student_edit, name='student_edit'),
    path('student/studentclick', studentclick_view),
    path('student/studentlogin',
         LoginView.as_view(template_name='student/studentlogin.html'), name='studentlogin'),
    path('student/studentsignup', student_signup_view, name='studentsignup'),
    path('student/student-dashboard',
         student_dashboard_view, name='student-dashboard'),
    path('student/student-exam', student_exam_view, name='student-exam'),
    path('student/take-exam/<int:pk>', take_exam_view, name='take-exam'),
    path('student/start-exam/<int:pk>', start_exam_view, name='start-exam'),
    path('student/calculate-marks', calculate_marks_view, name='calculate-marks'),
    path('student/view-result', view_result_view, name='view-result'),
    path('student/check-marks/<int:pk>', check_marks_view, name='check-marks'),
    path('student/student-marks', student_marks_view, name='student-marks'),
]

teacher = [
    path('teacher/teacherclick', teacherclick_view),
    path('staff/chat_lobby', staff_lobby, name='staff_chat_lobby'),
    path('teacher/teacherlogin',
         LoginView.as_view(template_name='teacher/teacherlogin.html'), name='teacherlogin'),
    path('teacher/addstudentlogin',
         LoginView.as_view(template_name='student/studentadded.html'), name='addstudentlogin'),
    path('teacher/addstudentsignup', add_student_signup_view,
         name='add_student_signup_view'),
    path('teacher/teachersignup', teacher_signup_view, name='teachersignup'),
    path('teacher/teacher-dashboard',
         teacher_dashboard_view, name='teacher-dashboard'),
    path('teacher/teacher-exam', teacher_exam_view, name='teacher-exam'),
    path('teacher/teacher-add-exam',
         teacher_add_exam_view, name='teacher-add-exam'),
    path('teacher/teacher-view-exam',
         teacher_view_exam_view, name='teacher-view-exam'),
    path('teacher/delete-exam/<int:pk>', delete_exam_view, name='delete-exam'),
    path('teacher/teacher-question',
         teacher_question_view, name='teacher-question'),
    path('teacher/teacher-add-question',
         teacher_add_question_view, name='teacher-add-question'),
    path('teacher/teacher-view-question',
         teacher_view_question_view, name='teacher-view-question'),
    path('teacher/see-question/<int:pk>',
         see_question_view, name='see-question'),
    path('teacher/remove-question/<int:pk>',
         remove_question_view, name='remove-question'),
]

exam = [

    path('logout', LogoutView.as_view(
        template_name='exam/logout.html'), name='logout'),
    path('contactus',  contactus_view),
    path('afterlogin',  afterlogin_view, name='afterlogin'),
    path('adminclick',  adminclick_view),
    path('adminlogin', LoginView.as_view(
        template_name='login/login.html'), name='adminlogin'),
    path('admin-dashboard',  admin_dashboard_view, name='admin-dashboard'),
    path('admin-teacher',  admin_teacher_view, name='admin-teacher'),
    path('admin-view-teacher',  admin_view_teacher_view, name='admin-view-teacher'),
    path('update-teacher/<int:pk>',  update_teacher_view, name='update-teacher'),
    path('delete-teacher/<int:pk>',  delete_teacher_view, name='delete-teacher'),
    path('admin-view-pending-teacher',  admin_view_pending_teacher_view,
         name='admin-view-pending-teacher'),
    path('admin-view-teacher-salary',  admin_view_teacher_salary_view,
         name='admin-view-teacher-salary'),
    path('approve-teacher/<int:pk>',
         approve_teacher_view, name='approve-teacher'),
    path('reject-teacher/<int:pk>',  reject_teacher_view, name='reject-teacher'),

    path('admin-student',  admin_student_view, name='admin-student'),
    path('admin-view-student',  admin_view_student_view, name='admin-view-student'),
    path('admin-view-student-marks',  admin_view_student_marks_view,
         name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>',
         admin_view_marks_view, name='admin-view-marks'),
    path('admin-check-marks/<int:pk>',
         admin_check_marks_view, name='admin-check-marks'),
    path('update-student/<int:pk>',  update_student_view, name='update-student'),
    path('delete-student/<int:pk>',  delete_student_view, name='delete-student'),

    path('admin-course',  admin_course_view, name='admin-course'),
    path('admin-add-course',  admin_add_course_view, name='admin-add-course'),
    path('admin-view-course',  admin_view_course_view, name='admin-view-course'),
    path('delete-course/<int:pk>',  delete_course_view, name='delete-course'),

    path('admin-question',  admin_question_view, name='admin-question'),
    path('admin-add-question',  admin_add_question_view, name='admin-add-question'),
    path('admin-view-question',  admin_view_question_view,
         name='admin-view-question'),
    path('view-question/<int:pk>',  view_question_view, name='view-question'),
    path('delete-question/<int:pk>',
         delete_question_view, name='delete-question'),


]


blog_url = [
    path('student_list_blog_course',
         student_list_blog_course, name='student_list_blog_course'),
    path('staff_list_blog_course',
         staff_list_blog_course, name='staff_list_blog_course'),
    path('list_blog', student_list_blog, name='student_list_blog'),
    path('staff_list_blog', staff_list_blog, name='staff_list_blog'),
    path('list_blog', teacher_list_blog, name='teacher_list_blog'),
    path('list_edit_blog', list_edit_blog, name='list_edit_blog'),
    path('view_blog/<str:pk>', view_blog, name='view_blog'),
    path('edit_blog/<str:pk>', edit_blog),
    path('create_blog', blog_edit, name='create_blog'),
    path('staff_create_blog', staff_create_blog, name='staff_create_blog'),
    path('save_blog', save_blog),
    path('delete_blog', delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>', save_edit_blog),

]

gallery_ = [

    path("gallery", gallery),
    path('image_upload_page_gallery', image_upload_page_gallery,
         name='image_upload_page_gallery'),
    path('upload_image', upload_image),
    path('delete_image', delete_image),

]


note = [
    path('course_list', course_list, name='course_list'),
    path('course/course_edit/<int:pk>', course_detail, name='course_detail'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/add/', course_add, name='course_add'),

    path('ebook/book_list/', book_list, name='book_list'),
    path('ebook/add/', ebook_add, name='ebook_add'),
    path('ebook/<int:pk>/edit/', ebook_edit, name='ebook_edit'),
    path('ebook/<int:pk>/delete/', ebook_delete, name='ebook_delete'),

    path('note/notes_list', notes_list, name='notes_list'),
    path('note/common_notes_list', common_notes_list, name='common_notes_list'),
    path('note/listout_notes', listout_notes, name='listout_notes'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
    path('note/create/', create_note, name='create_note'),
    path('note/<int:note_id>/update/', update_note, name='update_note'),
    path('note/<int:note_id>/delete/', delete_note, name='delete_note'),
]

event = [
    path('event_list', event_list, name='event_list'),
    path('event_add', event_add, name='event_add'),
    path('event_detail/<int:event_id>', event_detail, name='event_detail'),
    path('edit/<int:event_id>', event_edit, name='event_edit'),
    path('delete/<int:event_id>', event_delete, name='event_delete'),
    path('detail/<int:event_id>', event_detail, name='event_detail'),
]

dynamicFunctionality = [
    path('testimonicals_edit', Testimonicals_edit, name='testimonicals_edit'),
    path('testimonicals', Testimonicals, name='testimonicals'),
    path('testimonicals_save', Testimonicals_save, name='Testimonicals_save'),

]

AternativeUrls = [
    path('class_listout/<str:class_id>',
         get_class_peoples, name='class_listout'),
]

Staff_tool = [
    path('Staff_Staff_tool', Staff_Staff_tool),
    path('Staff_toolHome', Staff_toolHome),
    path('Staff_trans', Staff_translate_),
    path('Staff_convert_text', Staff_convert_text),
    path('Staff_wikipedia_summary', Staff_wikipedia_summary),
    path('Staff_convert_docx_to_pdf', Staff_convert_docx_to_pdf),
    path('Staff_convert_pdf_to_docx', Staff_convert_pdf_to_docx),
    path('Staff_convert_pdf_to_excel', Staff_convert_pdf_to_excel),
    path('Staff_convert_excel_to_pdf', Staff_convert_excel_to_pdf),
    path('Staff_convert_jpg_to_pdf', Staff_convert_jpg_to_pdf),
    path('Staff_convert_jpg_to_word', Staff_convert_jpg_to_word),
    path('Staff_calculator', Staff_calculator),
    path('Staff_cgpa_calculator', Staff_cgpa_calculator),
    path('Staff_handwriting_converter', Staff_handwriting_converter),
    path('Staff_keyword_to_image', Staff_keyword_to_image),
    path('Staff_video_meeting', Staff_video_meeting),

    path('Staff_gpa_calculator', Staff_gpa_calculator),
    path('Staff_get_subject', Staff_get_subject),
    path('Staff_Code_scriping', Staff_Code_scriping),
]

urlpatterns.extend(Make_Join([tools, common_tool, note, gallery_, blog_url, common, event,
                   admin, chatroom, classroom, videochat, studet, teacher, exam, dynamicFunctionality, alternative_url, Staff_tool]))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
