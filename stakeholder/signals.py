from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from stakeholder.models import Institution, Student, Parent,Teacher
from evaluation.models import StakeholderTag,InstitutionTag,Factor,Question
from django.contrib.auth.models import User
from nameparser import HumanName
from django.db import transaction

@receiver(pre_save, sender=Institution)
def create_admin_for_institution(sender, instance, *args, **kwargs):
    if instance.id is None:
        #creating admin for institution
        username = instance._username
        full_name = instance._full_name
        email = instance._email
        password = instance._password

        name = HumanName(full_name)
        first_name = name.first
        last_name = name.last

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        instance.institution_admin = user


@receiver(post_save, sender=Institution)
def create_factors_and_question_for_institution(sender, instance, created, *args, **kwargs):
    if created:
        #creating factors for institutions
        stakeholder_tag = StakeholderTag.objects.all()
        institution_tag = InstitutionTag.objects.all()

        #stakeholders
        student = stakeholder_tag[0]
        teacher = stakeholder_tag[1]
        self = stakeholder_tag[2]
        parent = stakeholder_tag[3]
        administrator = stakeholder_tag[4]

        #institutions
        primary = institution_tag[0]
        secondary = institution_tag[1]
        tertiary = institution_tag[2]

        with transaction.atomic():

            #Student Engagement Factor
            Student_Engagement = Factor(name="Student Engagement",description = "'Student engagement' assesses how effective the teacher is in creating a stimulating and interactive classroom environment that promotes active learning and student involvement.",institution = instance)
            Student_Engagement.save()
            Student_Engagement.institution_tag.add(tertiary,secondary)
            Student_Engagement.stakeholder_tag.add(student)

            question_1 = Question(question="The teacher encourage student to participate in class discussions and activities.",factor=Student_Engagement)
            question_1.save()
            question_1.stakeholder_tag.add(student)
            question_1.institution_tag.add(secondary,tertiary)

            question_2 = Question(question="The teacher make learning fun and enjoyable.",factor=Student_Engagement)
            question_2.save()
            question_2.stakeholder_tag.add(student)
            question_2.institution_tag.add(secondary,tertiary)


            #Learning outcomes Factor
            Learning_Outcomes = Factor(name="Learning Outcomes",description = "'Learning outcomes' assesses the extent to which the teacher has been successful in imparting knowledge and skills to the students and improving their academic performance.",institution = instance)
            Learning_Outcomes.save()
            Learning_Outcomes.institution_tag.add(tertiary,secondary,primary)
            Learning_Outcomes.stakeholder_tag.add(student,self)

            question_3 = Question(question="Does the teacher help you understand the material and difficult concepts effectively?",factor=Learning_Outcomes)
            question_3.save()
            question_3.stakeholder_tag.add(student)
            question_3.institution_tag.add(secondary,tertiary)

            question_4 = Question(question="Do you measure and assess student progress and achievement in your class?",factor=Learning_Outcomes)
            question_4.save()
            question_4.stakeholder_tag.add(self)
            question_4.institution_tag.add(secondary,tertiary)

            question_5 = Question(question="The teacher provide meaningful feedback to students to help them improve their learning.",factor=Learning_Outcomes)
            question_5.save()
            question_5.stakeholder_tag.add(student)
            question_5.institution_tag.add(secondary,tertiary)


            #Classroom management factor
            Classroom_Management = Factor(name="Classroom Management",description = "'Classroom management' assesses the extent to which the teacher is able to establish rules, routines, and procedures that facilitate effective teaching and learning while minimizing disruptions and behavioral problems.",institution = instance)
            Classroom_Management.save()
            Classroom_Management.institution_tag.add(tertiary,secondary,primary)
            Classroom_Management.stakeholder_tag.add(student,teacher,parent,self)


            question_6 = Question(question="Does the teacher establish and maintain a positive classroom environment?",factor=Classroom_Management)
            question_6.save()
            question_6.stakeholder_tag.add(student)
            question_6.institution_tag.add(secondary,tertiary)

            question_7 = Question(question="Does the teacher provide clear and concise directions for activities and assignments?",factor=Classroom_Management)
            question_7.save()
            question_7.stakeholder_tag.add(student)
            question_7.institution_tag.add(secondary,tertiary)

            question_8 = Question(question="Do you manage disruptive behavior or conflicts in the classroom effectively?",factor=Classroom_Management)
            question_8.save()
            question_8.stakeholder_tag.add(self)
            question_8.institution_tag.add(primary,secondary,tertiary)

            question_9 = Question(question="The teacher use a variety of instructional strategies, technologies and resources to support student learning.",factor=Classroom_Management)
            question_9.save()
            question_9.stakeholder_tag.add(student,teacher)
            question_9.institution_tag.add(secondary,tertiary)

            question_10 = Question(question="Does the teacher effectively handle conflicts or disciplinary issues with students?",factor=Classroom_Management)
            question_10.save()
            question_10.stakeholder_tag.add(teacher,parent)
            question_10.institution_tag.add(primary,secondary)

            question_11 = Question(question="Does the teacher keep parents informed about classroom rules and expectations, and actively involve them in improving classroom management?",factor=Classroom_Management)
            question_11.save()
            question_11.stakeholder_tag.add(parent)
            question_11.institution_tag.add(primary)


            #Communication skills factor
            Communication_Skills = Factor(name="Communication Skills",description = "'Communication skills' assesses the clarity, coherence, and appropriateness of the teacher's verbal and written communication, as well as the ability to actively listen and respond to others.",institution = instance)
            Communication_Skills.save()
            Communication_Skills.institution_tag.add(tertiary,secondary,primary)
            Communication_Skills.stakeholder_tag.add(student,teacher,parent,administrator)


            question_12 = Question(question="Does the teacher listen to and respond to students' questions and concerns?",factor=Communication_Skills)
            question_12.save()
            question_12.stakeholder_tag.add(student)
            question_12.institution_tag.add(secondary,tertiary)

            question_13 = Question(question="Does the teacher attend and perform in oraginizational seminers?",factor=Communication_Skills)
            question_13.save()
            question_13.stakeholder_tag.add(teacher,administrator)
            question_13.institution_tag.add(primary,secondary,tertiary)

            question_14 = Question(question="Does the teacher communicate with you regularly about your child's progress and academic performance?",factor=Communication_Skills)
            question_14.save()
            question_14.stakeholder_tag.add(parent)
            question_14.institution_tag.add(primary,secondary)

            question_15 = Question(question="Do you feel comfortable reaching out to the teacher with questions or concerns?",factor=Communication_Skills)
            question_15.save()
            question_15.stakeholder_tag.add(parent)
            question_15.institution_tag.add(primary,secondary)






@receiver(pre_save, sender=Student)
def create_user_for_student(sender, instance, *args, **kwargs):
    if instance.id is None:
        first_name = instance.first_name
        last_name = instance.last_name
        email = instance.email
        username = instance._student_username
        password = instance._student_password

        user = User(username=username, first_name=first_name, last_name=last_name, email = email)
        user.set_password(password)
        user.save()

        instance.user = user

@receiver(post_save, sender=Student)
def create_post_save_parent_for_student(sender, instance, created, *args, **kwargs):
    if created:
        parents_username = instance._parent_username
        phone_number = instance._parent_phone_number
        password = instance._parent_password

        user = User(username=parents_username)
        user.set_password(password)
        user.save()

        parent = Parent(user=user, phone_number=phone_number,institution = instance.institution,student = instance)
        parent.save()


@receiver(pre_save, sender=Teacher)
def create_user_for_teacher(sender, instance, *args, **kwargs):
    if instance.id is None:
        first_name = instance.first_name
        last_name = instance.last_name
        email = instance.email
        username = instance._teacher_username
        password = instance._teacher_password

        user = User(username=username, first_name=first_name, last_name=last_name, email = email)
        user.set_password(password)
        user.save()

        instance.user = user