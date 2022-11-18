from django.db import models


# Create your models here.
class Restaurant(models.Model):
    res_name = models.CharField(max_length=100)
    res_address = models.CharField(max_length=100)
    res_road_address = models.CharField(max_length=100)
    res_tel = models.CharField(max_length=30, blank=True, null=True)
    res_link = models.URLField(null=True, blank=True)
    res_stars = models.FloatField(null=True, blank=True)
    res_summary = models.CharField(max_length=200, null=True, blank=True)
    res_description = models.TextField(null=True, blank=True)
    res_find = models.CharField(max_length=200, null=True, blank=True)
    res_payment = models.CharField(max_length=50, null=True, blank=True)
    res_comfortables = models.CharField(max_length=200, null=True, blank=True)
    res_thumbnail = models.ImageField(upload_to='images/restaurant', blank=True, null=True)
    res_sub_thumbnail1 = models.ImageField(upload_to='images/restaurant', blank=True, null=True)
    res_sub_thumbnail2 = models.ImageField(upload_to='images/restaurant', blank=True, null=True)
    res_sub_thumbnail3 = models.ImageField(upload_to='images/restaurant', blank=True, null=True)
    def __str__(self):
        return self.res_name

class Menu(models.Model):
    menu_fk = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    menu = models.JSONField(null=True)

    def __str__(self):
        return 'menu'
    
class Store(models.Model):
    store_id = models.AutoField(primary_key=True) # store_id
    site= models.TextField(null=True)
    site_id = models.IntegerField(unique=True)
    store_name= models.TextField(null=True)
    micro_review= models.TextField(null=True)
    avg_rating= models.FloatField(null=True)
    main_image_url= models.TextField(null=True)
    tel= models.TextField()
    thumbnail = models.TextField(null=True)
    address = models.TextField(null=True)
    road_address = models.TextField(null=True)
    abbr_address = models.TextField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    visit_review_count = models.IntegerField(null=True)
    blog_review_count = models.IntegerField(null=True)
    biz_hour_info = models.TextField(null=True)
    create_date = models.DateField(null=True)
    def __str__(self):
        return self.store_name
    
  
class Store_menu(models.Model):
    menu_id = models.BigAutoField(primary_key=True)
    menu_name= models.TextField(null=True)
    menu_price= models.IntegerField(null=True)
    menu_image= models.TextField(null=True)
    menu_desc= models.TextField(null=True)
    store= models.ForeignKey(Store, to_field='site_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.menu_name
# class BusinessHour(models.Model):
#     fk = models.OneToOne
    


class Category(models.Model):
    category = models.TextField()
    sub_category = models.TextField()
    def _str_(self):
        return self.category