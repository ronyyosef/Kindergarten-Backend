from cleanup.helpers import clean_cognito_user_pool, clean_all_dynamodb, \
    clean_all_s3

clean_cognito_user_pool()
clean_all_dynamodb()
clean_all_s3()
print('finish cleanup')
