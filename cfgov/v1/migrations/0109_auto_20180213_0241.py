# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailsnippets.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import v1.blocks
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0108_auto_20180213_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublandingpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to bottom of text introduction.', required=False, label=b'Has bottom rule'))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links')), (b'video', wagtail.wagtailcore.blocks.StructBlock([(b'id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'E.g., in "https://www.youtube.com/watch?v=en0Iq8II4fA", the ID is everything after the "?v=".', required=False, label=b'ID')), (b'url', wagtail.wagtailcore.blocks.CharBlock(help_text=b'You must use the embed URL, e.g., https://www.youtube.com/embed/JPTg8ZB3j5c?autoplay=1&enablejsapi=1', required=False, label=b'URL')), (b'height', wagtail.wagtailcore.blocks.CharBlock(default=b'320', required=False)), (b'width', wagtail.wagtailcore.blocks.CharBlock(default=b'568', required=False))]))])), (b'info_unit_group', wagtail.wagtailcore.blocks.StructBlock([(b'format', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Choose the number and width of info unit columns.', choices=[(b'50-50', b'50/50'), (b'33-33-33', b'33/33/33'), (b'25-75', b'25/75')], label=b'Format')), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'If this field is not empty, the Heading field must also be set.', required=False)), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", default=True, required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of info unit group.', default=False, required=False)), (b'lines_between_items', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to show horizontal rule lines between info units.', default=False, required=False, label=b'Show rule lines between items')), (b'info_units', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'text', v1.blocks.HeadingTextBlock(required=False)), (b'level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'h2', b'H2'), (b'h3', b'H3'), (b'h4', b'H4')])), (b'icon', v1.blocks.HeadingIconBlock(help_text=b'Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#icons">See full list of icons</a>', required=False))], default={b'level': b'h3'}, required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))]))), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', required=False, label=b'Include sharing links?')), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))])), (b'image_text_25_75_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", default=False, required=False)), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])))])), (b'image_text_50_50_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", default=False, required=False)), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', required=False, label=b'Include sharing links?')), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))])), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'image_inset', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'right', b'right'), (b'left', b'left')])), (b'is_image_decorative', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Image decorative')), (b'image_width', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Default is 270px.', choices=[(170, b'170px'), (270, b'270px')], label=b'Image Width')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Bottom Rule'))])), (b'reusable_text', v1.blocks.ReusableTextChooserBlock(b'v1.ReusableText'))])), (b'half_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'third_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'post_preview_snapshot', wagtail.wagtailcore.blocks.StructBlock([(b'limit', wagtail.wagtailcore.blocks.CharBlock(help_text=b'How many posts do you want to show?', default=b'3', label=b'Limit')), (b'post_date_description', wagtail.wagtailcore.blocks.CharBlock(default=b'Published'))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'contact', wagtail.wagtailcore.blocks.StructBlock([(b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(b'v1.Contact')), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Add a horizontal rule line to top of contact block.', default=False, required=False))])), (b'formfield_with_button', wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'reg_comment', wagtail.wagtailcore.blocks.StructBlock([(b'document_id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Federal Register document ID number to which the comment should be submitted. Should follow this format: CFPB-YYYY-####-####', required=True, label=b'Document ID')), (b'generic_regs_link', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If unchecked, the link to comment at Regulations.gov if you want to add attachments will link directly to the document given above. Leave this checked if this comment form is being published before the full document is live at Regulations.gov, then uncheck it when the full document has been published.', default=True, required=False, label=b'Use generic Regs.gov link?')), (b'id', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Sets the `id` attribute in the form's markup. If not set, the form will be assigned a base id of `o-reg-comment_` with a random number appended.", required=False, label=b'Form ID'))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))])), (b'snippet_list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to top of snippet list.', default=False, required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'actions_column_width', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Choose the width in % that you wish to set the Actions column in a snippet list.', required=False, choices=[(b'70', b'70%'), (b'66', b'66%'), (b'60', b'60%'), (b'50', b'50%'), (b'40', b'40%'), (b'33', b'33%'), (b'30', b'30%')], label=b'Width of "Actions" column')), (b'snippet_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=v1.atomic_elements.organisms.get_snippet_type_choices)), (b'show_thumbnails', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"If selected, each snippet in the list will include a 150px-wide image from the snippet's thumbnail field.", required=False)), (b'actions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link_label', wagtail.wagtailcore.blocks.CharBlock(help_text=b'E.g., "Download" or "Order free prints"')), (b'snippet_field', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Corresponds to the available fields for the selected snippet type.', choices=v1.atomic_elements.organisms.get_snippet_field_choices))]))), (b'tags', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Tag'), help_text=b'Enter tag names to filter the snippets. For a snippet to match and be output in the list, it must have been tagged with all of the tag names listed here. The tag names are case-insensitive.'))])), (b'content_block', wagtail.wagtailcore.blocks.StructBlock([(b'margin_top', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Margin top. Defaults to 60px.', choices=[(b'default', b'Default'), (b'u-mt45', b'45px'), (b'u-mt30', b'30px'), (b'u-mt15', b'15px'), (b'u-mt15', b'15px'), (b'u-mt0', b'0px')])), (b'margin_bottom', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Margin bottom. Defaults to 60px.', choices=[(b'default', b'Default'), (b'u-mb45', b'45px'), (b'u-mb30', b'30px'), (b'u-mb15', b'15px'), (b'u-mb0', b'0px')])), (b'has_background', wagtail.wagtailcore.blocks.BooleanBlock(classname=b'background-input', help_text=b'Add gray background to block.', default=False, required=False)), (b'has_border_top', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Top border')), (b'has_border_bottom', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Bottom border')), (b'has_border_left', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Left border')), (b'has_border_right', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Right border')), (b'block_content', wagtail.wagtailcore.blocks.StreamBlock([(b'row', wagtail.wagtailcore.blocks.StructBlock([(b'equal_height_columns', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'columns', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'column_width', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Width of column. Defaults to 1.', required=False, choices=[(b'1-4', b'1/4'), (b'1-3', b'1/3'), (b'1-2', b'1/2'), (b'2-3', b'2/3'), (b'3-4', b'3/4'), (b'1', b'1')])), (b'column_content', wagtail.wagtailcore.blocks.StreamBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'snippet', v1.blocks.ReusableTextChooserBlock(b'v1.ReusableText')), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), (b'card', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'body', wagtail.wagtailcore.blocks.CharBlock(required=True))])), (b'email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Disclaimer')), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')])), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))]), required=False, icon=b'mail'))]))], icon=b'cogs'))])))]))], icon=b'cogs'))]))], blank=True),
        ),
    ]
