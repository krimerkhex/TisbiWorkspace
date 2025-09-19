from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm
from .models import User


def register_page(request):
    form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Регистрация успешна!',
                'user': {
                    'id': user.id,
                    'login': user.login,
                    'email': user.email
                }
            })
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'success': False,
                'errors': errors
            }, status=400)

    return JsonResponse({'error': 'Метод не разрешен'}, status=405)


def users_list(request):
    users = User.objects.all().values('id', 'login', 'email', 'created_at')
    return JsonResponse({'users': list(users)})