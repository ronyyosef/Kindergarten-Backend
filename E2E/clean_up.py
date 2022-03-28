from shared.hanlders.TeacherHandler import TeacherHandler


def clean_up_e2e(teacher_id):
    TeacherHandler.delete_teacher(teacher_id=teacher_id)
