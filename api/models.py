from django.db import models


# Create your models here.
class AssessmentResponse(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    responses = models.JSONField()
    predicted_condition = models.CharField(max_length=50)

    def __str__(self):
        return f"API {self.id} - self.predicted_condition"
