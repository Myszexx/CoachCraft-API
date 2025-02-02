from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'rfr': str(refresh),
        'acc': str(refresh.access_token),
    }