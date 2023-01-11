def update_projects(instance, validated_data):
    if projects := validated_data.get('projects', None):
        for project in instance.projects.all():
            project.organization = None
            project.save()

        for project in projects:
            project.organization = instance
            project.save()