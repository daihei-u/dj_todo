
from todo.models import Category,Tag,Status,Todo,Confidentioal
from registration.models import User
Category.objects.create(name="Todo")
Category.objects.create(name="Mission")
Category.objects.create(name="Regular work")
Status.objects.create(name="01.Proposal")
Status.objects.create(name="02.Plannning")
Status.objects.create(name="03.Building")
Status.objects.create(name="04.Go-Live")
Status.objects.create(name="05.Observation")
Status.objects.create(name="06.Closing")
Confidentioal.objects.create(name="S")
Confidentioal.objects.create(name="A")
Confidentioal.objects.create(name="B")
Confidentioal.objects.create(name="C-")
Confidentioal.objects.create(name="None")
Category.save
Status.save
Confidentioal.save
