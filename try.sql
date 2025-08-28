Select id from user u
where not exists ( Select 1 from user u2 where u.id = u2.id )