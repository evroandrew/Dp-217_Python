from enrollment_assistant.services import produce_message
from users.models import CustomUser


def remind_about_housing():
    for user in CustomUser.objects.filter(is_relocating=True):
        if True:
            produce_message(topic='send_email',
                            partition={'user_email': user.email,
                                       'subject': 'Enrollment assistant - Relocation',
                                       'message': 'Не забудьте що вам нема де жити!'})
