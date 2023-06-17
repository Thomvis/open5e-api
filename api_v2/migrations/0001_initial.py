# Generated by Django 3.2.19 on 2023-06-17 14:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArmorType',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('grants_stealth_disadvantage', models.BooleanField(default=False, help_text='If the armor results in disadvantage on stealth checks.')),
                ('strength_score_required', models.IntegerField(help_text='Strength score required to wear the armor without penalty.', null=True)),
                ('ac_base', models.IntegerField(help_text='Integer representing the armor class without modifiers.')),
                ('ac_add_dexmod', models.BooleanField(default=False, help_text='If the final armor class includes dexterity modifier.')),
                ('ac_cap_dexmod', models.IntegerField(help_text='Integer representing the dexterity modifier cap.', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the Document.', max_length=100, primary_key=True, serialize=False)),
                ('author', models.TextField(help_text='Author or authors.')),
                ('published_at', models.DateTimeField(help_text='Date of publication, or null if unknown.')),
                ('permalink', models.URLField(help_text='Link to the document.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the License.', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Organization.', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('damage_type', models.CharField(choices=[('bludgeoning', 'bludgeoning'), ('piercing', 'piercing'), ('slashing', 'slashing')], help_text='The damage type dealt by attacks with the weapon.', max_length=100)),
                ('damage_dice', models.CharField(help_text='The damage dice when used making an attack.', max_length=100)),
                ('versatile_dice', models.CharField(default=0, help_text='The damage dice when attacking using versatile.\nA value of 0 means that the weapon does not have the versatile property.', max_length=100)),
                ('range_reach', models.IntegerField(default=5, help_text='The range of the weapon when making a melee attack.', validators=[django.core.validators.MinValueValidator(0)])),
                ('range_normal', models.IntegerField(default=0, help_text='The normal range of a ranged weapon attack.\nA value of 0 means that the weapon cannot be used for a ranged attack.', validators=[django.core.validators.MinValueValidator(0)])),
                ('range_long', models.IntegerField(default=0, help_text='The long range of a ranged weapon attack.\nA value of 0 means that the weapon cannot be used for a long ranged attack.', validators=[django.core.validators.MinValueValidator(0)])),
                ('is_finesse', models.BooleanField(default=False, help_text='If the weapon is finesse.')),
                ('is_thrown', models.BooleanField(default=False, help_text='If the weapon is thrown.')),
                ('is_two_handed', models.BooleanField(default=False, help_text='If the weapon is two-handed.')),
                ('requires_ammunition', models.BooleanField(default=False, help_text='If the weapon requires ammunition.')),
                ('requires_loading', models.BooleanField(default=False, help_text='If the weapon requires loading.')),
                ('is_heavy', models.BooleanField(default=False, help_text='If the weapon is heavy.')),
                ('is_light', models.BooleanField(default=False, help_text='If the weapon is light.')),
                ('is_lance', models.BooleanField(default=False, help_text='If the weapon is a lance.')),
                ('is_net', models.BooleanField(default=False, help_text='If the weapon is a net.')),
                ('is_simple', models.BooleanField(default=False, help_text='If the weapon category is simple.')),
                ('is_improvised', models.BooleanField(default=False, help_text='If the weapon is improvised.')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MagicItemType',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('requires_attunement', models.BooleanField(default=False, help_text='If the item requires attunement.')),
                ('rarity', models.IntegerField(choices=[(1, 'common'), (2, 'uncommon'), (3, 'rare'), (4, 'very rare'), (5, 'legendary')], help_text='Integer representing the rarity of the object.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('size', models.IntegerField(choices=[(1, 'Tiny'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Huge'), (6, 'Gargantuan')], help_text='Integer representing the size of the object.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('weight', models.DecimalField(decimal_places=3, help_text='Number representing the weight of the object.', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('armor_class', models.IntegerField(help_text='Integer representing the armor class of the object.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('hit_points', models.IntegerField(help_text='Integer representing the hit points of the object.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('damage_immunities', models.JSONField(default=list, help_text='List of damage types that this is immune to.')),
                ('damage_resistances', models.JSONField(default=list, help_text='List of damage types that this is resistant to.')),
                ('damage_vulnerabilities', models.JSONField(default=list, help_text='List of damage types that this is vulnerable to.')),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, help_text='Number representing the cost of the object.', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('armor_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.armortype')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
                ('magic_item_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.magicitemtype')),
                ('weapon_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.weapontype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='license',
            field=models.ForeignKey(help_text='License that the content was released under.', on_delete=django.db.models.deletion.CASCADE, to='api_v2.license'),
        ),
        migrations.AddField(
            model_name='document',
            name='organization',
            field=models.ForeignKey(help_text='Organization which has written the game content document.', on_delete=django.db.models.deletion.CASCADE, to='api_v2.organization'),
        ),
        migrations.AddField(
            model_name='armortype',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document'),
        ),
    ]
