from config import TOKEN
import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


user_data = []


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


logger = logging.getLogger(__name__)


FULLNAME, PHONE_NUMBER, MESSAGE = range(3)


def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['About Us', 'Our Courses', 'Payment']]

    update.message.reply_text(
        'Assalom alaykum! isystem IT Akademiyasining rasmiy telegram botiga xush kelibsiz! isystem - IT olamidagi sizning ko\'makdoshingiz.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
    )


def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Bizga qiziqish bildirganiz uchun tashakkur! O\'ylaymizku siz bilan yana ko\'rishamiz. Xayr salomat bo\'ling'
    )
    return ConversationHandler.END


# Main menu
def aboutUs(update: Updater, context: CallbackContext) -> None:
    update.message.reply_html(
        'Bizning akademiyamiz axborot texnologiyalarining barcha tendensiyalari bilan yaqindan tanishtiradi. Shinam o\'quv binosi va zamonaviy texnologiyalarga asoslangan kurslar dasturi bilan yurtimizning eng yirik, xalqaro kompaniyalarida IT karyerangizni boshlaysiz.\n'
        '<b>Maqsadimiz:</b>\n Raqobatbardosh malakali kadrlarni yetishtirish. Ish beruvchi sizni emas, siz ishni tanlang!\n'
        '<b>Dasturlashni o\'rganish:</b>\nDasturlash asoslarini, Python, C#, Java, PHP yoki Go tillarini o\'rganasiz...\n'
        '<b>Vaqtingizni tejash:</b>\nJahon standartlariga mos keluvchi o\'quv dasturlarimiz sizning ham vaqtingizni, ham naqdingizni tejaydi.\n'
        '<b>Do\'stona atmosfera:</b>\nZamonaviy offisimizda mentorlaringiz va hamrohlaringiz bilan o\'qish jarayoni yanada qiziqarli va mazmunli 👋\n'
        '<b>24/7 qo\'llab-quvvatlash:</b>\nKursni muvaffaqiyatli tugatib, yirik kompaniyalarda yuqori daromad topishingizgacha bo\'lgan yo\'lda sizga yelkadosh bo\'lamiz\n'
    )
    update.message.delete()


def ourCourses(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Foundation', 'Programming', 'Android'], ['Front-End', 'Back-End','Data Science', '.NET'], ['Main menu']]

    update.message.reply_text(
        'Siz o\'qimoqchi bo\'lgan kursni tanlang',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
        )
    update.message.delete()


# Courses
def foundation(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>Foundation</b>\nMaktab yoshidagilar uchun Scratch, C/C++ tillarida dasturlash asoslarini va turli amaliy mashg\'ulotlar bilan mantiqiy fikrlashni o\'rgatamiz.\n'
        '<b>Kurs davomiyligi:</b> 3 oy/haftada 3 kun\n'
        '<b>Jami to\'lov:</b> 1,800,000\n',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
        )
    user_data.append(update.message.text)
    update.message.delete()


def programming(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>Programming</b>\nDasturlash asoslarini, OOP va uning imkoniyatlarini C++, Java, Python va C# tillarida o\'rgatamiz.\n'
        '<b>Kurs davomiyligi:</b> 4 oy/haftada 3 kun\n'
        '<b>Jami to\'lov:</b> 3,200,000\n', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    user_data.append(update.message.text)
    update.message.delete()


def android(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>Android</b>\nAndroid dasturlash darslar davomida Java va Kotlin dasturlash tili, Ma\'lumotlar bazasi, REST API, Firebase, Git texnalogiyalari va android dasturlash sohasida qo\'llaniladigan eng so\'nggi texnalogiyalardan foydalanish, Android Smartphone, Android TV va WearOS lar uchun dastur yozishni, moslashuvchan UI yig\'ishni o\'rgansiz.\n'
        '<b>Kurs davomiyligi:</b> 6 oy/haftada 3 kun\n'
        '<b>Jami to\'lov:</b> 7,200,000\n',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    user_data.append(update.message.text)
    update.message.delete()


def front_end(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>Front-End</b>\nWeb va Responsive Mobile sahifalarni tayyorlash, JavaScript tilini chuqur o\'rganish va VueJS/ReactJS asosida SPA va SSR dasturlarni tayyorlashni o\'rganasiz.\n'
        '<b>Kurs davomiyligi:</b> 4 oy/haftada 3 kun\n'
        '<b>Jami to\'lov:</b> 3,600,000\n', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    user_data.append(update.message.text)
    update.message.delete()


def back_end(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>Back-End</b>\nPython, C#, Java, PHP yoki Golang tillari asosida monolit va microservice\'larni qurish, turli API va web dasturlarni yaratishni o\'rgansiz.\n'
        '<b>Kurs davomiyligi:</b> 4 oy/haftada 3 kun\n'
        '<b>Jami to\'lov:</b> 4,800,000\n', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    user_data.append(update.message.text)
    update.message.delete()


def data_science(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>Data Science</b>\nMa\'lumotlar muhandisligi - injinerligi kursimiz sizga Data Science va AI asoslarini, Machine Learning amaliy qo\'llanishi, algoritmlar va ularning qo\'llanilishini o\'rgatadi\n'
        '<b>Kurs davomiyligi:</b> 7 oy/haftada 4 kun\n'
        '<b>Jami to\'lov:</b> 16,800,000\n', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    user_data.append(update.message.text)
    update.message.delete()


def dot_net(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['Registration', 'Back']]

    update.message.reply_html(
        '<b>.NET</b>\n9 oy davomida intensiv Backend, Frontend, Monolit, Microservis kabi professional skillar amaliy o\'rgatiladi. Kurs davomida hayotiy proyektlar ustida ishlanadi va portfolio yig\'ib boriladi. Kursni tamomlagach, jamoaga qo\'shilish imkoni yoki ishga kirishda amaliy ko\'mak beriladi\n'
        '<b>Kurs davomiyligi:</b> 9 oy/haftada 5 kun\n'
        '<b>Jami to\'lov:</b> 19,800,000\n', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    user_data.append(update.message.text)
    update.message.delete()


def mainMenu(update: Updater, context: CallbackContext) -> None:
    reply_keyboard = [['About Us', 'Our Courses', 'Payment']]

    update.message.reply_text(
        reply_keyboard=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    update.message.delete()


# Registration


def registration(update: Updater, context: CallbackContext) -> None:
    update.message.reply_text(
        'Ism-familyangizni kiriting: ',
        reply_markup=ReplyKeyboardRemove()
    )
    update.message.delete()
    return FULLNAME


def full_name(update: Updater, context: CallbackContext):
    update.message.reply_text(
        'Telefon raqamingizni kiritng: '
    )
    user_data.append(update.message.text)
    return PHONE_NUMBER


def phone_number(update: Updater, context: CallbackContext):
    update.message.reply_text(
        'Qaysi kursda o\'qimoqchisiz '
    )
    user_data.append(update.message.text)
    return MESSAGE


def message(update: Updater, context: CallbackContext):
    user_data.append(update.message.text)
    update.message.reply_text(
        'Tabriklaymiz!!! Siz ro\'yhatdan muvaffaqiyatli o\'tdingiz. Tez orada operatorlarimiz siz bilan bog\'lanishadi',
        f'Sizning ma\'lumotlaringiz:\nKurs nomi: {user_data[0]}\nIsm-familyangiz: {user_data[1]}\n Telefon raqamingiz: {user_data[2]}\nComment: {user_data[3]}',
    )
    #update.message.forward()
    return ConversationHandler.END


# Run
def main() -> None:
    """Run the bot."""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(MessageHandler(Filters.regex('^About Us$'), aboutUs))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Our Courses$'), ourCourses))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Foundation$'), foundation))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Programming$'), programming))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Android$'), android))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Front-End$'), front_end))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Back-End$'), back_end))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Data Science$'), data_science))
    dispatcher.add_handler(MessageHandler(Filters.regex('^.NET$'), dot_net))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Main menu$'), start))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Back$'), ourCourses))

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^Registration$'), registration)],
        states={
            FULLNAME: [MessageHandler(Filters.text & ~Filters.command, full_name)],
            PHONE_NUMBER: [MessageHandler(Filters.text & ~Filters.command, phone_number)],
            MESSAGE: [MessageHandler(Filters.text & ~Filters.command, message)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
