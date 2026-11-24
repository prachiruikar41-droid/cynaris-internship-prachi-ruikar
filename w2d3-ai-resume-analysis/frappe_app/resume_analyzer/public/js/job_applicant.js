
frappe.ui.form.on("Job Applicant", {
    refresh: function(frm) {
        if (!frm.is_new() && frm.doc.resume_attachment) {
            frm.add_custom_button("Generate AI Resume Summary", function() {
                frappe.call({
                    method: "resume_analyzer.ai_resume_analyzer.api.generate_resume_summary",
                    args: {
                        applicant_id: frm.doc.name
                    },
                    freeze: true,
                    freeze_message: "Analyzing resume with AI...",
                    callback: function(r) {
                        if (r.message && r.message.success) {
                            frm.set_value(
                                "ai_resume_summary",
                                r.message.summary
                            );

                            frappe.show_alert({
                                message: "Resume summary generated using " +
                                    r.message.provider,
                                indicator: "green"
                            });

                            frm.refresh_field("ai_resume_summary");
                        }
                    }
                });
            });
        }
    }
});
