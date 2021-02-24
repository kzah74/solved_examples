from privileges import Admin

admin = Admin('kristiyan', 'alexiev', 'krisal', 'krisal@abv.bg', 'sofia')
admin.describe_user()

admin_privileges = [
            'can delete profile',
            'can add profile',
            'can remove comments',
            ]

admin.privileges.privileges = admin_privileges

print("\nThe admin " + admin.username + " has these privileges:")
admin.privileges.show_privileges()
