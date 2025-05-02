def user_listing_path(instance, filename):
    return 'listings {0}/{1}'.format(instance.seller.user.id, filename)
