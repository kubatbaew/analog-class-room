document.addEventListener("DOMContentLoaded", () => {
    initScripts();
});

function initScripts() {
    toggleMenuButtons();
    setupActions();
    setupDeleteModal();
    setupSorting();
    setupEditModal(); // Добавляем обработку открытия editModalGroup
}

const btnAddStudentToGroupCancel = document.getElementById('cancel-add-student-btn')
const editModalGroup = document.getElementById("editModalGroup");
const openPanelAddStudent = document.getElementById('open-panel-add-student')

openPanelAddStudent.addEventListener('click', () => {
    editModalGroup.style.display = "flex";
})

btnAddStudentToGroupCancel.addEventListener('click', () => {
    editModalGroup.style.display = "none";
})


function togglePassword() {
    let passwordInput = document.getElementById("password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";// Измените иконку на "скрыть"
    } else {
        passwordInput.type = "password"; // Верните иконку "показать"
    }
}

// Функция для открытия/закрытия меню действий
function setupActions() {
    document.querySelectorAll('.actions > a').forEach(actionButton => {
        actionButton.addEventListener('click', (e) => {
            e.preventDefault();

            // Найти ближайший .actions-menu
            const menu = actionButton.closest('.actions').querySelector('.actions-menu');

            // Закрыть все меню перед открытием нужного
            document.querySelectorAll('.actions-menu').forEach(m => m.classList.add('opa-hidden'));

            // Переключить текущее меню
            if (menu) {
                menu.classList.toggle('opa-hidden');
            }
        });
    });

    // Закрытие меню при клике вне его
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.actions-menu') && !e.target.closest('.actions > a')) {
            document.querySelectorAll('.actions-menu').forEach(menu => {
                menu.classList.add('opa-hidden');
            });
        }
    });
}

// Функция для работы с кнопками меню
function toggleMenuButtons() {
    const menuNoHover = document.getElementById('active-logo-no-hover');
    const menuHover = document.getElementById('active-logo-hover');
    const menuClick = document.getElementById('active-logo-click');
    const menuClickHover = document.getElementById('active-logo-click-hover');

    if (!menuNoHover || !menuHover || !menuClick || !menuClickHover) {
        return; // Выход, если элементы не найдены
    }

    menuClick.style.display = "none";
    menuHover.style.display = "none";
    menuClickHover.style.display = "none";

    menuNoHover.addEventListener("mouseover", () => {
        menuHover.style.display = "block";
    });

    menuHover.addEventListener("mouseout", () => {
        menuHover.style.display = "none";
    });

    menuHover.addEventListener("click", () => {
        menuNoHover.style.display = "none";
        menuHover.style.display = "none";
        menuClick.style.display = "block";
    });

    menuClick.addEventListener("click", () => {
        menuClick.style.display = "none";
        menuHover.style.display = "none";
        menuNoHover.style.display = "block";
    });
}

// Функция сортировки работ
function setupSorting() {
    const selectBox = document.getElementById('order-select');
    if (!selectBox) return;

    selectBox.addEventListener("change", () => {
        const selectedValue = selectBox.value;
        document.querySelectorAll(".theme-work").forEach(theme => {
            theme.style.display = (selectedValue === "all" || theme.id === selectedValue) ? "block" : "none";
        });
        document.querySelectorAll(".student-works-item-grid").forEach(theme => {
            theme.style.display = (selectedValue === "all" || theme.id === selectedValue) ? "flex" : "none";
        });
    });
}

// Функция удаления элемента
function setupDeleteModal() {
    const modal = document.getElementById("deleteModal");
    const confirmDelete = document.getElementById("confirmDelete");
    const cancelDelete = document.getElementById("cancelDelete");
    let itemToDelete = null;

    document.querySelectorAll(".action-item").forEach(button => {
        button.addEventListener("click", function () {
            if (this.textContent.trim() === "Удалить") {
                itemToDelete = this.closest(".item, .item-work"); // Учитываем оба класса
                if (modal) modal.style.display = "flex";
            }
        });
    });

    if (cancelDelete) {
        cancelDelete.addEventListener("click", () => {
            if (modal) modal.style.display = 'none';
            itemToDelete = null;
        });
    }

    if (confirmDelete) {
        confirmDelete.addEventListener("click", () => {
            if (itemToDelete) {
                // itemToDelete.remove();
                itemToDelete = null;
                if (modal) modal.style.display = 'none';
            }
        });
    }
}

// Функция открытия модального окна редактирования
function setupEditModal() {
    const editModalGroup = document.getElementById("editModalGroup");
    const cancelChange = document.getElementById("cancelChange");

    if (!editModalGroup) return;

    document.querySelectorAll(".action-item").forEach(button => {
        button.addEventListener("click", function () {
            if (this.textContent.trim() === "Изменить") {
                const parentItem = this.closest(".item, .item-work"); // Ищем родительский элемент
                const itemId = parentItem ? parentItem.getAttribute("id") : null;

                if (itemId) {
                    editModalGroup.setAttribute("data-item-id", itemId); // Сохраняем ID внутри модального окна
                }

                editModalGroup.style.display = "flex"; // Показываем модальное окно
            }
        });
    });

    if (cancelChange) {
        cancelChange.addEventListener("click", () => {
            editModalGroup.style.display = "none";
        });
    }
}


const bannerInput = document.getElementById('bannerInput');
const bannerPreview = document.getElementById('bannerPreview');
const saveButton = document.querySelector('.save');

bannerInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            bannerPreview.src = e.target.result;
            saveButton.disabled = false; // Активируем кнопку "Сохранить"
        };
        reader.readAsDataURL(file);
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.getElementById("item-edit-btn-banner");
    const modal2 = document.querySelector(".modal-window-for-upload-banner2");
    const modal = document.querySelector(".modal-window-for-upload-banner");
    const cancelButton = modal.querySelector(".cancel");
    const bannerInput = document.getElementById("bannerInput");
    const bannerPreview = document.getElementById("bannerPreview");
    const saveButton = modal.querySelector(".save");

    // Открытие модального окна
    editButton.addEventListener("click", function () {
        modal.style.display = "block";
        modal2.style.display = "block";

    });

    // Закрытие модального окна
    cancelButton.addEventListener("click", function (event) {
        event.preventDefault();
        modal.style.display = "none";
        modal2.style.display = "none";
    });

    // Отслеживание загрузки файла и отображение превью
    bannerInput.addEventListener("change", function () {
        const file = bannerInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                bannerPreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
            saveButton.removeAttribute("disabled"); // Активируем кнопку "Сохранить"
        }
    });
});