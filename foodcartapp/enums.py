from django.db import models


class OrderStatus(models.TextChoices):
    NEW = "new", "Необработанный"
    PREPARING = "preparing", "Готовится"
    DELIVERING = "delivering", "В доставке"
    DONE = "done", "Доставлен"
    CANCELED = "canceled", "Отменен"
