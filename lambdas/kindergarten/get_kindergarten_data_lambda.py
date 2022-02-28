
from const import ID, FIRST_NAME, LAST_NAME, PHOTO_LINK, KINDERGARTEN_ID, GROUP_NUMBER, EMAIL, PHONE_NUMBER, IS_ADMIN, \
    TEACHERS, CHILDREN
from utils.logger import logger

teacher1 = {
    ID: '56',
    FIRST_NAME: 'rony',
    LAST_NAME: 'yosef',
    PHOTO_LINK: 'data:image/jpeg;base64,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',
    KINDERGARTEN_ID: '1',
    GROUP_NUMBER: '1',
    EMAIL: "rony@gmail.com",
    PHONE_NUMBER: "05102154",
    IS_ADMIN: "Yes"
}
teacher2 = {
    ID: '56B',
    FIRST_NAME: 'ronyB',
    LAST_NAME: 'yosef',
    PHOTO_LINK: 'data:image/jpeg;base64,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',
    KINDERGARTEN_ID: '1',
    GROUP_NUMBER: '1',
    EMAIL: "rony@gmail.com",
    PHONE_NUMBER: "05102154",
    IS_ADMIN: "Yes"
}
children1 = {
    ID: '4B',
    FIRST_NAME: 'daveB',
    LAST_NAME: 'keissarB',
    PHOTO_LINK: 'data:image/jpeg;base64,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',
    KINDERGARTEN_ID: '1',
    GROUP_NUMBER: '1',
}
children2 = {
    ID: '4B',
    FIRST_NAME: 'dave',
    LAST_NAME: 'keissar',
    PHOTO_LINK: 'data:image/jpeg;base64,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',
    KINDERGARTEN_ID: '1',
    GROUP_NUMBER: '1',
}


def get_kindergarten_data(event, context):
    result = {
        TEACHERS: [
            teacher1,
            teacher2
        ],
        CHILDREN: [
            children1,
            children2
        ]
    }
    return result
