let NewUserPage = function() {
   let onTheFlyFunctions = function() {
      let addCompanyBtn = $('#addCompanyBtn');
      let addDepartmentBtn = $('#addDepartmentBtn');
      let cancelAddCompanyBtn = $('<a href="#" class="btn btn-sm btn-alt-primary ml-20"><i class="fa fa-fw fa-undo"></i></a>');
      let cancelAddDepartmentBtn = $('<a href="#" class="btn btn-sm btn-alt-primary ml-20"><i class="fa fa-fw fa-undo"></i></a>');
      let newDepartmentInput = $("<input type='text' class='form-control' name='departmentsSelect' id='departmentsSelect'>");
      let newCompanyInput = $("<input type='text' class='form-control' name='companiesSelect' id='companiesSelect'>");
      let companiesLabel = $('label[for=companiesSelect]');
      let departmentsLabel = $('label[for=departmentsSelect]');
      let companiesSelect = $('#companiesSelect');
      let departmentsSelect = $('#departmentsSelect');
      let depatmentsList = $('#departmentsList');
      let companyInput = $('#company');
      let departmentInput = $('#department');
      let companiesSelections = [];
      let departmentsSelections = [];
      companiesSelect.on('change', function() {
         let companyId = this.value;
         let departmentsOptions = depatmentsList.find(`option[data-company-id=${companyId}]`).clone();
         let departmentsCurrentOptions = departmentsSelect.children();
         if (departmentsCurrentOptions.length > 1) {
            departmentsCurrentOptions.slice(1).remove();
         }
         departmentsSelect.append(departmentsOptions);
         departmentsSelect.removeAttr('disabled');
         addDepartmentBtn.removeClass('disabled');
         companyInput.val(this.value);
      });
      departmentsSelect.on('change', function() {
         departmentInput.val(this.value);
      });
      addCompanyBtn.on('click', function() {
         companiesSelections.push(companiesSelect, companiesSelect.next());
         departmentsSelections.push(departmentsSelect, departmentsSelect.next());
         companiesSelect.next().detach();
         companiesSelect.detach();
         departmentsSelect.next().detach();
         departmentsSelect.detach();
         addCompanyBtn.detach();
         addDepartmentBtn.detach();
         newCompanyInput.val('');
         newDepartmentInput.val('');
         newCompanyInput.insertBefore(companiesLabel);
         cancelAddCompanyBtn.insertAfter(companiesLabel);
         newDepartmentInput.insertBefore(departmentsLabel);
      });
      cancelAddCompanyBtn.on('click', function() {
         newCompanyInput.detach();
         cancelAddCompanyBtn.detach();
         companiesSelections.forEach(function(selection) {
            selection.insertBefore(companiesLabel);
         });
         addCompanyBtn.insertAfter(companiesLabel);
         newDepartmentInput.detach();
         departmentsSelections.forEach(function(selection) {
            selection.insertBefore(departmentsLabel);
         });
         addDepartmentBtn.insertAfter(departmentsLabel);
         companiesSelections = [];
         departmentsSelections = [];
         companyInput.val(companiesSelect.val());
      });
      addDepartmentBtn.on('click', function() {
         departmentsSelections.push(departmentsSelect, departmentsSelect.next());
         departmentsSelect.next().detach();
         departmentsSelect.detach();
         addDepartmentBtn.detach();
         addCompanyBtn.detach();
         newDepartmentInput.val('');
         newDepartmentInput.insertBefore(departmentsLabel);
         cancelAddDepartmentBtn.insertAfter(departmentsLabel);
      });
      cancelAddDepartmentBtn.on('click', function() {
         newDepartmentInput.detach();
         cancelAddDepartmentBtn.detach();
         departmentsSelections.forEach(function(selection) {
            selection.insertBefore(departmentsLabel);
         });
         addDepartmentBtn.insertAfter(departmentsLabel);
         addCompanyBtn.insertAfter(companiesLabel);
         departmentsSelections = [];
         departmentInput.val(departmentsSelect.val());
      });
      newCompanyInput.on('change', function() {
         companyInput.val(this.value);
      });
      newDepartmentInput.on('change', function () {
         departmentInput.val(this.value);
      });
   };
   let cleaveInputs = function() {
      new Cleave('#phone_number', {
         phone: true,
         phoneRegionCode: 'US',
         prefix: "+1"
      });
   };

   return {
      init() {
         onTheFlyFunctions();
         cleaveInputs();
      }
   }
}();
$(function () {
   NewUserPage.init();
});