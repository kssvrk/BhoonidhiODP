from django.db import models

# Create your models here.

class ProcessGroup(models.Model):
    group_name=models.CharField(max_length=100,unique=True)
    group_description=models.CharField(max_length=5000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return f"name:{self.group_name}"

class ProcessCatalogue(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    created_by = models.CharField(max_length=50)
    command = models.CharField(max_length=500)
    docker_image = models.CharField(max_length=500)
    cpu = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    cpu_limit = models.CharField(max_length=50,default="500m")
    memory_limit = models.CharField(max_length=50,default='256MiB')
    process_name=models.CharField(max_length=100,unique=True)
    process_id=models.AutoField(primary_key=True)
    group_id=models.ManyToManyField(ProcessGroup,related_name='processes')
    process_description=models.CharField(max_length=3000,blank=True,null=True)

    def __str__(self):
        return f"name:{self.process_name},image: {self.docker_image},command:{self.command}"


class Status(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=1000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return f"name:{self.name}"

class Job(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    finished_at = models.DateTimeField(blank=True,null=True)
    process=models.ForeignKey(ProcessCatalogue,on_delete=models.RESTRICT)
    exit_code=models.IntegerField()
    status=models.ForeignKey(Status,on_delete=models.RESTRICT)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    created_by = models.CharField(max_length=50)
    reason = models.CharField(max_length=500)
    arguments = models.JSONField()
    job_id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"name:{self.process},job_id: {self.job_id}"
