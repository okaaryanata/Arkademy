function loading(button) {
    console.log(button)
    $(button).addClass('hide')
    $('#loading').removeClass('hide')
}
function getAllUser() {
    $.ajax({
        method: 'GET',
        url: 'http://localhost:5000/get-all-user',
        success: function (res) {
            JSON.parse(res).forEach(function (data) {
                $('#tabel-user').append(`
                <tr>
                    <td>
                        <table>
                            <tr id="bord">
                                <td>
                                    <p>${data.name}</p>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <p>
                                    ${data.skills}
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td>
                        <div class="input-group mb-3">
                            <input id="add_skill${data.user_id}" type="text" class="form-control" placeholder="Add Skill" aria-label="Recipient's username" aria-describedby="basic-addon2">
                            <div class="input-group-append">
                                <button type="submit" class="btn btn-primary" onclick="addSkill(${data.user_id})">Add Skill</button>
                            </div>
                        </div>
                    </td>
                </tr>
                `)
            })
        },
        error: function (err) {
            console.log(err)
        }
    })
}

function addUser() {
    $.ajax({
        method: 'POST',
        url: "http://localhost:5000/add-user",
        beforeSend: function (req) {
            req.setRequestHeader('Content-Type', 'application/json')
        },
        data: JSON.stringify({
            "username": $('#add_user').val()
        }),
        success: function (res) {
            console.log("sukses")
            alert("Sukses tambah Programmer")
            window.location = "index.html"
        },
        error: function (err) {
            alert("gagal " + this.status)
            console.log(err)
        }
    })
}

function addSkill(id) {
    $.ajax({
        method: 'POST',
        url: "http://localhost:5000/add-skill",
        beforeSend: function (req) {
            req.setRequestHeader('Content-Type', 'application/json')
        },
        data: JSON.stringify({
            "skill": $('#add_skill'+id).val(),
            "user_id": id
        }),
        success: function (res) {
            console.log("sukses")
            alert("Sukses tambah skill")
            window.location = "index.html"
        },
        error: function (err) {
            alert("Gagal " + this.status)
            console.log(err)
        }
    })
}