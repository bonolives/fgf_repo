from django.db import models
from django.contrib.auth.models import User

# Choices for life_form field
LIFE_FORM_CHOICES = [
    ('forest', 'Forest'),
    ('meadow', 'Meadow'),
    ('climber', 'Climber'),
    ('grassland', 'Grassland'),
    ('herb', 'Herb'),
    ('shrub', 'Shrub'),
    ('tree', 'Tree'),
]

REGION_CHOICES = [
    ('northern_uganda', 'Northern Uganda'),
    ('eastern_uganda', 'Eastern Uganda'),
    ('western_uganda', 'Western Uganda'),
    ('central_uganda', 'Central Uganda'),

]

class Language(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    # General information
    botanical_name = models.CharField(max_length=100, blank=True, null=True)
    english_name = models.CharField(max_length=100, blank=True, null=True)
    region_in_Uganda = models.CharField(max_length=100, choices=REGION_CHOICES, null=True)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    life_form = models.CharField(max_length=100, choices=LIFE_FORM_CHOICES, null=True)
    
    description = models.TextField(null=True, blank=True)
     
    climate_impact = models.TextField(null=True, blank=True)
    
    # Values and properties
    social_value = models.TextField(null=True, blank=True)
    economical_value = models.TextField(null=True, blank=True)
    cultural_value = models.TextField(null=True, blank=True)
    other_value = models.TextField(null=True, blank=True)
    
    # Not used for now
    is_medicinal = models.BooleanField(blank=True, null=True)
    # Multimedia
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    video = models.FileField(upload_to='plant_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='plant_audio/', blank=True, null=True)
    
    # Notes
    notes = models.TextField(null=True, blank=True)
    # contributor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contributor_name = models.CharField(max_length=255, null=True, blank=True) 
    citation = models.TextField(null=True, blank=True) 
     
    # Associated names in different languages
    names = models.ManyToManyField(Language, through='PlantName', related_name='botanical_name')
    
    #PK added since all plants are medicinal
    health_issues = models.TextField(null=True, blank=True)
    part_used = models.CharField(max_length=100, blank=True, null=True)
    preparation_steps = models.TextField(null=True, blank=True)
    dosage = models.CharField(max_length=100, blank=True, null=True)
    contraindications = models.TextField(null=True, blank=True)
    shelf_life = models.CharField(max_length=100, blank=True, null=True)

    local_language = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Plant: {self.botanical_name}"

class PlantName(models.Model):
    # plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plant_names')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    local_language = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Plant Name: {self.name} - Language: {self.language}"

#not used for now
class MedicinalPlant(models.Model):
    # Associated plant information
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, related_name='medicinal_info')
    #PK added
    #is_medicinal = models.BooleanField(auto_created=True, blank=True, null=True)
    # Medicinal information
    health_issues = models.TextField()
    part_used = models.CharField(max_length=100, blank=True, null=True)
    preparation_steps = models.TextField()
    dosage = models.CharField(max_length=100, blank=True, null=True)
    contraindications = models.TextField()
    shelf_life = models.CharField(max_length=100, blank=True, null=True)
    
    #notes = models.TextField()
    #contributor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    
    # Associated names in different languages
    names = models.ManyToManyField(Language, through='MedicinalPlantName', related_name='medicinal_plant_names')

    def __str__(self):
        return f"Medicinal Info for Plant: {self.plant.botanical_name}"

#Not used
class MedicinalPlantName(models.Model):
    medicinal_plant = models.ForeignKey(MedicinalPlant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Medicinal Plant Name: {self.name} - Language: {self.language}"
