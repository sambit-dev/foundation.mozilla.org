# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 18:05
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0022_auto_20180511_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modularpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')]))))), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('figure', wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False))))), ('figuregrid', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('figuregrid2', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button'), ('btn-success', 'Success button'), ('btn-info', 'Info button'), ('btn-warning', 'Warning button'), ('btn-danger', 'Danger button'), ('btn-ghost', 'Ghost button')])), ('outline', wagtail.core.blocks.BooleanBlock(default=False, required=False))))), ('spacer', wagtail.core.blocks.StructBlock((('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')])),))), ('quote', wagtail.core.blocks.StructBlock((('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock()))))),))), ('pulse_listing', wagtail.core.blocks.StructBlock((('search_terms', wagtail.core.blocks.CharBlock(help_text='Fill in any number of pulse entry search terms (separated by spaces).')), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=0, help_text='The maximum number of results to fetch (use 0 for default maximum of 48)', min_value=0, required=False)), ('newest_first', wagtail.core.blocks.BooleanBlock(default=True, help_text='Check this box to list entries "newest first".', required=False)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this box to only get results from the featured entry list.', required=False))))))),
        ),
        migrations.AlterField(
            model_name='primarypage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')]))))), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('figure', wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False))))), ('figuregrid', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('icon', 'Constrain to 100x100'), ('small', 'Constrain to 200x200'), ('medium', 'Constrain to 400x400'), ('large', 'Constrain to 800x800'), ('original', 'Use original dimensions')])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('figuregrid2', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button'), ('btn-success', 'Success button'), ('btn-info', 'Info button'), ('btn-warning', 'Warning button'), ('btn-danger', 'Danger button'), ('btn-ghost', 'Ghost button')])), ('outline', wagtail.core.blocks.BooleanBlock(default=False, required=False))))), ('spacer', wagtail.core.blocks.StructBlock((('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')])),))), ('quote', wagtail.core.blocks.StructBlock((('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock()))))),))), ('pulse_listing', wagtail.core.blocks.StructBlock((('search_terms', wagtail.core.blocks.CharBlock(help_text='Fill in any number of pulse entry search terms (separated by spaces).')), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=0, help_text='The maximum number of results to fetch (use 0 for default maximum of 48)', min_value=0, required=False)), ('newest_first', wagtail.core.blocks.BooleanBlock(default=True, help_text='Check this box to list entries "newest first".', required=False)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this box to only get results from the featured entry list.', required=False))))))),
        ),
    ]