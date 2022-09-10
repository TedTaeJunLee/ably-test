# Generated by Django 4.1.1 on 2022-09-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PhoneValidationCode",
            fields=[
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="삭제 여부"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="삭제일"),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                ("phone", models.CharField(max_length=30, verbose_name="개인 전화번호")),
                ("code", models.CharField(max_length=6, verbose_name="인증번호")),
                ("expire_at", models.DateTimeField(verbose_name="인증번호 만료일")),
                ("is_used", models.BooleanField(default=False, verbose_name="사용 여부")),
                (
                    "use_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="인증번호 사용일"
                    ),
                ),
            ],
            options={
                "verbose_name": "핸드폰 번호 인증",
                "verbose_name_plural": "핸드폰 번호 인증 목록",
                "db_table": "phone_validation_code",
                "unique_together": {("phone", "code")},
            },
        ),
    ]